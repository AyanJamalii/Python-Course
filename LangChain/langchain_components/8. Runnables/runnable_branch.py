from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

prompt_1 = PromptTemplate(
    template='Write a detailed report on topic. {topic}',
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template='Summarize the following text 3 proper paragraphs. \n {text}.',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt_1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())> 200, RunnableSequence(prompt_2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic': 'AI VS HI'}))