import os
import warnings
from dotenv import load_dotenv
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load environment variables from .env file
load_dotenv()

def get_youtube_data(video_id):
    # Read API key directly from environment variables
    youtube_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=youtube_key)
    
    video_response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()
    
    title = video_response['items'][0]['snippet']['title']
    
    # Extract transcript using YouTubeTranscriptApi
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    full_transcript = " ".join([item['text'] for item in transcript_list])
    
    return f"Title: {title}\n\nTranscript:\n{full_transcript}"

# 1. Fetch Video Data (Replace with your target Video ID, e.g., "dQw4w9WgXcQ")
video_id = "J5_-l7WIO_w"
raw_text = get_youtube_data(video_id)

# 2. Text Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.create_documents([raw_text])

# 3. Vector Embeddings & Storage (Automatically picks GOOGLE_API_KEY from environment)
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 4. LLM & Prompt Pipeline (Automatically picks GOOGLE_API_KEY from environment)
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer the user question based ONLY on the provided YouTube video transcript context.

Context:
{context}

Question: {question}
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 5. RAG Chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 6. Execute Query
query = "What is the main topic discussed in this video?"
response = rag_chain.invoke(query)

print("Response:\n", response)