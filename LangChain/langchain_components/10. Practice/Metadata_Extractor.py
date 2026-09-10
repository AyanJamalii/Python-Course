from typing import List
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

class ProductInfo(BaseModel):
    product_name: str = Field(description="Name of the Product.") 
    price: float = Field(description="Price of the Product")
    category: str = Field(description="Category of the Product")
    in_stock: bool = Field(description="Is the item currently in stock?")
    features: List[str] = Field(description="List of key features")

structured_llm = model.with_structured_output(ProductInfo)

prompt = PromptTemplate(
    template="Extract the product information from this text. \n{description}",
    input_variables=["description"]
)

product_input = input("Enter about your Product: ").strip()
chain = prompt | structured_llm
response = chain.invoke({"description": product_input})
print(response)
