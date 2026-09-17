import os
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=DeprecationWarning)
load_dotenv()

from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. YouTube Data Fetching
video_url = "https://www.youtube.com/watch?v=J5_-l7WIO_w&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=17"
loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=False)
docs = loader.load()

# 2. Text Splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

# 3. Embeddings & Vector Store Setup
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# 4. Retriever Setup
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. LLM Setup
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer the user question based ONLY on the provided YouTube transcript context.

Context:
{context}

Question: {question}
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 6. RAG Chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 7. Query Execution
query = "What are the key points discussed in the video?"
response = rag_chain.invoke(query)

print("Response:\n", response)