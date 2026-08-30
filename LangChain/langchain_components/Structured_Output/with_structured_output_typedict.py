from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list."]
    summary: Annotated[str, "A breif summary of the review."]
    sentiment: Annotated[str, "Return sentiment of th ereview either negative, positive or neutral."]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list."]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list."]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The user describes the Samsung Galaxy S24 Ultra as a powerful device driven by the Snapdragon 8 Gen 3 processor, which handles heavy gaming, multitasking, and photo editing smoothly. The 5000mAh battery easily provides a full day of heavy usage, complemented by 45W fast charging.

Key features include the built-in S-Pen for quick note-taking or sketching, and a 200MP camera setup that excels in low-light night mode. While the camera supports up to 100x zoom, image clarity drops noticeably beyond 30x.

On the downside, the phone's bulk and weight make single-handed operation awkward. The reviewer notes that Samsung's One UI still includes pre-installed duplicate apps that overlap with Google services, and considers the $1,300 retail price quite steep.

Pros:
Highly capable processor suitable for gaming and intensive tasks
Excellent 200MP camera system with strong zoom features
Reliable, long battery endurance coupled with fast charging
Integrated S-Pen functionality

Cons:
Large, heavy form factor that hinders one-handed usability
Presence of duplicate pre-installed software (bloatware) in One UI
High price point compared to competing flagships""")

print(result)
print(result['summary'])
print(result['sentiment'])