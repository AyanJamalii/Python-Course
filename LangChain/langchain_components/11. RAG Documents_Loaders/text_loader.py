from langchain_community.document_loaders import TextLoader
loader = TextLoader('text.txt',)

docs = loader.load()
print(type(docs))
print(len(docs))
print(docs[0])
