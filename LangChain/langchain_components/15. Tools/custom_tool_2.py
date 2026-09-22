from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests
import os
from langchain_core.tools import InjectedToolArg
from typing import Annotated

load_dotenv()

# tool create

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversation factor between a given base currency and target currency"""

    url = f"https://v6.exchangerate-api.com/v6/{os.getenv('EXCHANGE_RATE_API_KEY')}/pair/{base_currency}/{target_currency}"

    response = requests.get(url)
    return response.json()


print(get_conversion_factor.invoke({'base_currency': 'PKR', 'target_currency': 'USD'}))


@tool
def convert(base_currency: int, conversation_rate: Annotated[float, InjectedToolArg]) -> float:
    """given a currency conversion rate this function calculate the target currency value from a given base currency value"""

    return base_currency * conversation_rate

print(convert.invoke({'base_currency': 10, 'conversation_rate':0.003605}))


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

messages = [
    HumanMessage('What is the conversion factor between usd and pkr and based on that can you convert 10 usd to pkr')
]
ai_message = llm_with_tools.invoke(messages)
print(ai_message.tool_calls)
