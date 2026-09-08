from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

prompt_extract = PromptTemplate(
    template="Extract the core issue topic in 2-3 words from this customer feedback:\n{feedback}",
    input_variables=["feedback"],
)


prompt_response = PromptTemplate(
    template="You are customer support. The customer reported an issue regarding '{topic}'.\nOriginal Feedback: {feedback}\nWrite a polite 2-sentence resolution response.",
    input_variables=["topic", "feedback"],
)

feedback_chain = prompt_extract | model | parser | (lambda x: {"topic" : x, "feedback": test_feedback}) | prompt_response | model | parser


test_feedback = "I ordered my shoes 10 days ago, but they still haven't arrived and the tracking status is stuck."
result = feedback_chain.invoke({'feedback': test_feedback})
print(result)