# type: ignore
from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


# # schema
# class Review(TypedDict):
#     summary: str
#     sentiment: str


# schema
class Review(TypedDict):
    key_themes: Annotated[
        list[str], "Write down all the key themes discussed in the review"
    ]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
                                 Most modern smartphones come with powerful processors, ranging from Snapdragon 8 Gen 3 to MediaTek Dimensity 9400, ensuring smooth performance. RAM varies from 8GB to 16GB, which is great for multitasking. Cameras have improved significantly, with flagship models offering 200MP sensors, while mid-range phones stick to 50MP or 64MP setups. Battery life is solid, with most phones packing 5000mAh or more, supporting fast charging.
                                    """)

print(result)
