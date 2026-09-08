from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

prompt_1 = PromptTemplate(
    template="Extract the main topic from this question: {question}",
    input_variables=["question"],
)

prompt_2 = PromptTemplate(
    template="Give a 1-sentence tip about {topic}", input_variables=["topic"]
)

chain = (
    prompt_1
    | model
    | parser
    | (lambda x: {"topic": x})
    | prompt_2  
    | model
    | parser
)

result = chain.invoke({"question": "How can I improve my Python coding?"})
print(result)