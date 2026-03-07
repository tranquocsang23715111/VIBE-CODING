from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    birth_year: int
    major: str
    gpa: float

class StudentCreate(StudentBase):
    student_id: int

class Student(StudentBase):
    student_id: int

    class Config:
        orm_mode = True