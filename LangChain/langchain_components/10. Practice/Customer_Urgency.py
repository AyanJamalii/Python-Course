from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

# Step 1: Category aur Urgency extract karne ka prompt
prompt_extract = PromptTemplate(
    template="Analyze this feedback and return ONLY 'Category | Urgency':\nFeedback: {feedback}",
    input_variables=["feedback"],
)

# Step 3: Internal support note prompt
prompt_note = PromptTemplate(
    template="[INTERNAL ESCALATION NOTE]\nCategory: {category}\nUrgency: {urgency}\nCustomer Feedback: {original_feedback}\nRecommended Next Action: Write 1 clear action step for support staff.",
    input_variables=["category", "urgency", "original_feedback"],
)

# --- YOUR TASK ---
# Single LCEL chain banayein jo:
# 1. prompt_extract | model | parser se output laye ("Category | Urgency")
# 2. Lambda function se us string ko split('|') kare aur 'original_feedback' ke sath dict banaye
# 3. prompt_note | model | parser ko pipe kare


extracter_chain = prompt_extract | model | parser | (lambda x : {"category": x.split('|')[0].strip(), "urgency": x.split('|')[1].strip(), "original_feedback": test_feedback}) | prompt_note | model | parser


test_feedback = "I was double charged on my credit card for order #4092! Fix this immediately or I am reporting to my bank."
result_1 = extracter_chain.invoke({'feedback': test_feedback})
print(result_1)


