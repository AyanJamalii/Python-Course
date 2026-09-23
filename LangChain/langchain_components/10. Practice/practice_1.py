import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# 1. Define Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful programming assistant. Keep answers concise.",
        ),
        ("user", "Explain {topic} in 2 short sentences."),
    ]
)

# 2. Initialize Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.7)

# 3. Create Chain (LCEL Syntax)
chain = prompt | llm | StrOutputParser()

# 4. Invoke Chain
if __name__ == "__main__":
    result = chain.invoke({"topic": "LangChain"})
    print("Response:\n", result)