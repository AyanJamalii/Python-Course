from langchain_huggingface import HuggingFaceEmbeddings


embeddeing = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Islamabad is the capital of Pakistan."

result = embeddeing.embed_query(text)

print(str(result))