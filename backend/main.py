from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@app.post("/students")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# READ
@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentBase, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.student_id == student_id).first()

    if not db_student:
        return {"error": "Student not found"}

    db_student.name = student.name
    db_student.birth_year = student.birth_year
    db_student.major = student.major
    db_student.gpa = student.gpa

    db.commit()
    db.refresh(db_student)

    return db_student


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    db.delete(student)
    db.commit()
    return {"message": "Deleted"}