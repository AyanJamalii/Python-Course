from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage 
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

chat_history = [
    SystemMessage(content="you are a helpful Ai Assistant")
]

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
 
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)
    