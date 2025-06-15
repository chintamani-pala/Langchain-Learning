# type: ignore
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str = "kuna"
    age: Optional[int]
    email: EmailStr
    cgpa: float = Field(gt=0, lte=10)


new_student = {"name": "chintamani", "age": 22, "email": "abc@gmail.com", "cgpa": 10}

student = Student(**new_student)

print(student)
