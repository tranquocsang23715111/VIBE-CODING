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
class ClassBase(BaseModel):
    class_name: str
    advisor: str


class ClassCreate(ClassBase):
    pass


class Class(ClassBase):
    class_id: int

    class Config:
        orm_mode = True