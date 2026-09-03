from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt_1 = PromptTemplate(
    template='Generate a detail report on {topic}',
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text. \n {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

result = chain.invoke({'topic': 'Unemployment in Pakistan'})
print(result)