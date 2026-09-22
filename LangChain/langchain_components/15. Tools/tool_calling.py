from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

@tool
def multiply(a: int, b:int) -> int:
    """Given 2 numbers a and b this tool return their Product."""
    return a*b

print(multiply.invoke({"a": 5, "b": 3}))

# Tool Binding

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
llm_with_tools = llm.bind_tools([multiply])

llm_with_tools.invoke('how are you?')

query = HumanMessage('Can you multiply 3 with 11')
messages = [query]

result = llm_with_tools.invoke(messages)
messages.append(result)

fin = llm_with_tools.invoke(messages)
print(fin)