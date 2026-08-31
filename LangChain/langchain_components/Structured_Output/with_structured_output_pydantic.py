from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list.")
    summary: str = Field(description="A breif summary of the review.")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of th ereview either negative, positive or neutral.")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list.")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list.")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

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
High price point compared to competing flagships

Review by Ayan Jamali
""")

print(result)
