from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

res = search_tool.invoke("Top news in Pakistan, in 2 lines")
print("Result:\n", res)