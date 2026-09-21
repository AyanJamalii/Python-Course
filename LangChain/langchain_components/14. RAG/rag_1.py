import os
import re
import warnings
from urllib.parse import urlparse, parse_qs

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
    parsed_url = urlparse(video_url)

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        if parsed_url.path == "/watch":
            video_id = parse_qs(parsed_url.query).get("v")

            if video_id:
                return video_id[0]

        if parsed_url.path.startswith("/shorts/"):
            return parsed_url.path.split("/shorts/")[1].split("/")[0]

        if parsed_url.path.startswith("/embed/"):
            return parsed_url.path.split("/embed/")[1].split("/")[0]

    elif parsed_url.hostname in ["youtu.be", "www.youtu.be"]:
        return parsed_url.path.lstrip("/").split("/")[0]

    raise ValueError("Invalid YouTube URL")


def get_video_title(video_id):
    youtube_key = os.getenv("YOUTUBE_API_KEY")

    if not youtube_key:
        raise ValueError("YOUTUBE_API_KEY is missing from your .env file")

    youtube = build(
        "youtube",
        "v3",
        developerKey=youtube_key
    )

    response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()

    items = response.get("items", [])

    if not items:
        raise ValueError(f"Video not found: {video_id}")

    return items[0]["snippet"]["title"]


def get_youtube_data(video_url):
    video_id = extract_video_id(video_url)
    title = get_video_title(video_id)

    ytt_api = YouTubeTranscriptApi()

    transcript_list = ytt_api.list(video_id)

    transcripts = list(transcript_list)

    if not transcripts:
        raise ValueError("No transcripts are available for this video.")

    preferred_transcripts = []

    for transcript in transcripts:
        language_code = transcript.language_code

        if language_code == "en":
            preferred_transcripts.append(transcript)

    for transcript in transcripts:
        if transcript not in preferred_transcripts:
            preferred_transcripts.append(transcript)

    selected_transcript = preferred_transcripts[0]

    fetched_transcript = selected_transcript.fetch()

    full_transcript = " ".join(
        snippet.text for snippet in fetched_transcript
    )

    print(f"\nVideo: {title}")
    print(f"Transcript language: {selected_transcript.language}")
    print(f"Language code: {selected_transcript.language_code}")
    print(
        f"Type: "
        f"{'Auto-generated' if selected_transcript.is_generated else 'Manually created'}"
    )

    available_languages = [
        transcript.language
        for transcript in transcripts
    ]

    print(
        f"Available transcript languages: "
        f"{', '.join(available_languages)}"
    )

    return f"""
Title: {title}

Transcript language: {selected_transcript.language}

Transcript:
{full_transcript}
"""


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

Answer the user's question using only the provided
YouTube video transcript context.

The transcript may be in any language.
Understand the transcript and answer the user
in the same language as the user's question.

If the answer is not present in the transcript,
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
