from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


loader = DirectoryLoader(
    path='books', 
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)