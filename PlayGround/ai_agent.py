from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")



client = genai.Client(api_key=API_KEY)

class AiAgent: 
    def __init__(self, name, role):
        self.name = name
        self.role = role

        self.chat = client.chats.create(
            model="gemini-3.6-flash",
            config=types.GenerateContentConfig(
                system_instruction=(
                    f"You are {self.name}, a helpful Ai Agent working as {self.role}"
                    f" {self.role}"
                )
            ),
        )
    def ask(self, prompt):
        print(f"[{self.name}] is thinking....")

        response = self.chat.send_message(prompt)
        return response.text


ai_agent = AiAgent(name="Frey", role="Python Expert")
answer = ai_agent.ask("what do you think about Ai Future? answer me in 5 lines")

print("\n---- Ai Response ----")
print(answer)