from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Python is a high-level programming language known for readability and rich libraries.",
    "LangChain simplifies creating applications powered by large language models.",
    "Vector databases store high-dimensional embeddings for fast semantic similarity search.",
    "Islamabad is the capital city of Pakistan, located in the Federal Capital Territory.",
    "Mount Everest is the highest mountain above sea level, located in the Himalayas.",
    "Retrieval-Augmented Generation (RAG) combines external document retrieval with LLMs.",
    "Open-source models like Llama and Qwen allow running AI applications locally.",
    "Transformers are deep learning architectures designed for sequence processing.",
    "Docker packages applications into containers for consistent deployment across systems.",
    "Photosynthesis is the process plants use to convert sunlight into chemical energy."
]

query = "tell me about RAG."

docs_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], docs_embedding)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print(f"Similarity score is: {score}")

