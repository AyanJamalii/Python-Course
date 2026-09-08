from typing import Literal
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
str_parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Give the sentiment of the feedback"
    )


pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt_1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive, negative, or neutral.\n{feedback}\n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": pydantic_parser.get_format_instructions()
    },
)

classifier_chain = prompt_1 | model | pydantic_parser

prompt_apology = PromptTemplate(
    template="Write a short 2-sentence empathetic apology response for this negative customer feedback:\n{feedback}",
    input_variables=["feedback"],
)

prompt_highlight = PromptTemplate(
    template="Summarize the main product highlight from this review in 1 short bullet point under 15 words:\n{feedback}",
    input_variables=["feedback"],
)

# 4. Action Branch Chain
action_branch = RunnableBranch(
    (
        lambda x: x["sentiment"].sentiment == "negative",
        prompt_apology | model | str_parser,
    ),
    (
        lambda x: x["sentiment"].sentiment in ["positive", "neutral"],
        prompt_highlight | model | str_parser,
    ),
    RunnableLambda(lambda x: "Could not process response."),
)

full_chain = (
    RunnableParallel(
        {
            "sentiment": classifier_chain,
            "feedback": lambda x: x["feedback"],  
        }
    )
    | RunnableParallel(
        {
            "sentiment": lambda x: x["sentiment"].sentiment,
            "action_taken": action_branch,
        }
    )
)

test_review_1 = "The battery life of this phone is awful and it heats up within 10 minutes of use."
test_review_2 = (
    "The camera quality is decent, but the delivery took a few extra days."
)

print("--- Test 1 Result ---")
print(full_chain.invoke({"feedback": test_review_1}))

print("\n--- Test 2 Result ---")
print(full_chain.invoke({"feedback": test_review_2}))