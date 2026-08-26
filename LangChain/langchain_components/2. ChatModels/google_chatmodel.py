import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
warnings.filterwarnings("ignore")

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

# Output parser content ko clean text mein extract kar deta hai
parser = StrOutputParser()
chain = model | parser

result = chain.invoke("What is the Capital of Pakistan?")

print(result)