from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template='Explain the following Joke. {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser = StrOutputParser()
chain = RunnableSequence(prompt, model, parser, prompt_2, model, parser)

print(chain.invoke({'topic': 'Human'}))