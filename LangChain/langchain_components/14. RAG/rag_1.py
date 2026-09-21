import os
import re
import warnings

from dotenv import load_dotenv
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


warnings.filterwarnings("ignore", category=DeprecationWarning)
load_dotenv()


def extract_video_id(video_url):
    patterns = [
        r"(?:youtube\.com/watch\?v=)([^&]+)",
        r"(?:youtu\.be/)([^?&]+)",
        r"(?:youtube\.com/shorts/)([^?&]+)",
        r"(?:youtube\.com/embed/)([^?&]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, video_url)

        if match:
            return match.group(1)

    raise ValueError("Invalid YouTube URL")


def get_youtube_data(video_url):
    video_id = extract_video_id(video_url)

    youtube_key = os.getenv("YOUTUBE_API_KEY")

    if not youtube_key:
        raise ValueError("YOUTUBE_API_KEY is missing from your .env file")

    youtube = build(
        "youtube",
        "v3",
        developerKey=youtube_key
    )

    video_response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()

    items = video_response.get("items", [])

    if not items:
        raise ValueError(f"Video not found: {video_url}")

    title = items[0]["snippet"]["title"]

    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(
        video_id,
        languages=["hi"]
        ).to_raw_data()

    full_transcript = " ".join(
        item["text"] for item in transcript
    )

    return f"Title: {title}\n\nTranscript:\n{full_transcript}"


video_url = input("Paste YouTube video URL: ").strip()

raw_text = get_youtube_data(video_url)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

splits = text_splitter.create_documents([raw_text])

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Answer the user's question only using the provided
YouTube video transcript context.

If the answer is not present in the context,
say that the information is not available in the transcript.

Context:
{context}

Question:
{question}
"""
)


def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)


query = input("Ask a question about the video: ").strip()

response = rag_chain.invoke(query)

print("\nResponse:\n")
print(response)

