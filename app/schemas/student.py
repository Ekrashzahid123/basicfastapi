from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=1, le=120)
    course: str = Field(..., min_length=2, max_length=60)


class Student(StudentCreate):
    id: int
