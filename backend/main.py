from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
import csv
from fastapi.responses import FileResponse



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
@app.post("/classes")
def create_class(class_data: schemas.ClassCreate, db: Session = Depends(get_db)):
    new_class = models.Class(**class_data.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class


# READ
@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@app.get("/classes")
def get_classes(db: Session = Depends(get_db)):
    return db.query(models.Class).all()

#tìm kiếm
@app.get("/students/search")
def search_student(name: str, db: Session = Depends(get_db)):
    students = db.query(models.Student).filter(models.Student.name.contains(name)).all()
    return students

@app.get("/classes/search")
def search_class(class_name: str, db: Session = Depends(get_db)):
    classes = db.query(models.Class).filter(models.Class.class_name.contains(class_name)).all()
    return classes

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

#tổng số sinh viên
@app.get("/stats/total_students")
def total_students(db: Session = Depends(get_db)):
    total = db.query(func.count(models.Student.student_id)).scalar()
    return {"total_students": total}

#GPA mean
@app.get("/stats/avg_gpa")
def avg_gpa(db: Session = Depends(get_db)):
    avg = db.query(func.avg(models.Student.gpa)).scalar()
    return {"average_gpa": avg}

#số sinh viên theo ngành
@app.get("/stats/by_major")
def students_by_major(db: Session = Depends(get_db)):
    result = db.query(
        models.Student.major,
        func.count(models.Student.student_id)
    ).group_by(models.Student.major).all()

    return [
        {"major": r[0], "total": r[1]}
        for r in result
    ]


#API:
@app.get("/export/csv")
def export_csv(db: Session = Depends(get_db)):

    students = db.query(models.Student).all()

    filename = "students.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Birth Year", "Major", "GPA"])

        for s in students:
            writer.writerow([
                s.student_id,
                s.name,
                s.birth_year,
                s.major,
                s.gpa
            ])

    return FileResponse(filename, media_type="text/csv", filename=filename)