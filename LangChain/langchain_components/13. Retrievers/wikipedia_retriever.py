import os
from dotenv import load_dotenv
from langchain_community.retrievers import WikipediaRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

retriever = WikipediaRetriever(top_k_results=2)

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context:

Context:
{context}

Question: {question}
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

response = chain.invoke("What is Quantum Computing?")
print(response)