import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    huggingfacehub_api_token=token,
    max_new_tokens=100,
    timeout=30
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("What is the capital of Pakistan?")
print(response.content)