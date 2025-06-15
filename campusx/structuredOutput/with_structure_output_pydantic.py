# # type: ignore
# from typing import Annotated, Optional, Literal
# from pydantic import BaseModel, Field
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


# # # schema
# # class Review(TypedDict):
# #     summary: str
# #     sentiment: str


# # schema
# class Review(BaseModel):
#     key_themes: list[str] = Field(
#         description="Write down all the key themes discussed in the review"
#     )
#     summary: str = Field(description="A brief summary of the review")
#     sentiment: Literal["pos", "neg"] = Field(
#         description="Return sentiment of the review"
#     )
#     pros: Optional[list[str]] = Field(
#         default=None, description="Write down all the pros inside a list"
#     )
#     cons: Optional[list[str]] = Field(
#         default=None, description="Write down all the cons inside a list"
#     )
#     name: Optional[str] = Field(description="Write the name of the reviewer")


# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""
#                                  Most modern smartphones come with powerful processors, ranging from Snapdragon 8 Gen 3 to MediaTek Dimensity 9400, ensuring smooth performance. RAM varies from 8GB to 16GB, which is great for multitasking. Cameras have improved significantly, with flagship models offering 200MP sensors, while mid-range phones stick to 50MP or 64MP setups. Battery life is solid, with most phones packing 5000mAh or more, supporting fast charging.
#                                     """)

# print(result)


# type: ignore
from typing import Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


# Define a minimal schema
class Review(BaseModel):
    summary: str = Field(description="Brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Sentiment of the review")
    key_themes: list[str] = Field(description="Key topics discussed in the review")


# Use structured output
structured_model = model.with_structured_output(Review)

# New review text
review_text = """
The Acer Swift X offers great value with its Ryzen 7 processor and RTX 3050 GPU. 
It handles gaming and creative tasks surprisingly well at this price point. 
However, the build quality feels a bit cheap and the display is just average.
"""

# Run the model and print result
result = structured_model.invoke(review_text)
print(result)
