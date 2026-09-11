from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('gk.pdf')

docs = loader.load()

print(len(docs))