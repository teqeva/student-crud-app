from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: str
    age: Optional[int]

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int
    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    course_name: str
    credits: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    course_id: int
    class Config:
        orm_mode = True

