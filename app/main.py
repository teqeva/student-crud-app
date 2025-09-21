from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency (DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Students
@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}


# Courses
@app.post("/courses", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@app.get("/courses", response_model=list[schemas.Course])
def read_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db)

@app.put("/courses/{course_id}", response_model=schemas.Course)
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.update_course(db, course_id, course)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.delete_course(db, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}
