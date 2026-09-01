from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser = JsonOutputParser()

template_1 = PromptTemplate(
    template ='Give me the name, age and city of a fictional person. \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template_1.format()

result = model.invoke(prompt)
final_result = parser.parse(result.content)

print(final_result)
print(type(final_result))
