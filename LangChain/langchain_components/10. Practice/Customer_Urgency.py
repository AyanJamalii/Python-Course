from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel, RunnableLambda

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

prompt_extract = PromptTemplate(
    template="Analyze this feedback and return ONLY 'Category | Urgency':\nFeedback: {feedback}",
    input_variables=["feedback"],
)
prompt_note = PromptTemplate(
    template="[INTERNAL ESCLATION NOTE]\n"
    "Reciept ID: {reciept_id}\n" 
    "Category: {category}\n" 
    "Urgency: {urgency}\n"
    "Customer Feedback: {original_feedback}\n\n"
    "Recommended Next Action: Write 1 clear, actionable step for the support team.",
    input_variables=["reciept_id", "category", "urgency", "original_feedback"],
)

user_reciept_id = input("Enter your Reciept/Order ID: ").strip()
user_feedback = input("Enter your Feedback here: ").strip()

feedback_chain = (
    RunnableParallel(
            {
                "extraction_raw": prompt_extract | model | parser,
                "reciept_id": lambda x: x["reciept_id"],
                "feedback": lambda x: x["feedback"],
            }
        )
            | RunnableLambda(
                lambda x: {
                    "reciept_id":   x["reciept_id"],
                    "category": x["extraction_raw"].split("|")[0].strip(),
                    "urgency": x["extraction_raw"].split("|")[1].strip(),
                    "original_feedback": x["feedback"],
                }
            )
    
    | prompt_note
    | model
    | parser
)

result = feedback_chain.invoke(
    {
        "reciept_id": user_reciept_id,
        "feedback": user_feedback
    }
)

print("\n" + "=" * 40)
print(result)
print("=" * 40)


