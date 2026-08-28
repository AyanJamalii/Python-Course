from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

chat_history = []

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
 
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)
    