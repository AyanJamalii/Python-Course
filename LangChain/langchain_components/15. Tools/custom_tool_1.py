from langchain_community.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

res = multiply.invoke({"a": 3, "b": 5})
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(res)

# LANGCHAIN IS COMPLETED

# WILL BE MOVING TOWards LangGraph NOW :)