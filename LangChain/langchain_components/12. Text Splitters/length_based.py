from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader('gk.pdf') 

docs = loader.lazy_load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

print(splitter.split_documents(docs))
