from typing import Dict, List

from fastapi import APIRouter, HTTPException, status

from app.schemas.student import Student, StudentCreate

router = APIRouter(prefix="/students", tags=["students"])

students_db: Dict[int, Student] = {}
_student_id_counter = 1


@router.get("/", response_model=List[Student])
def get_students():
    return list(students_db.values())


@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    global _student_id_counter

    new_student = Student(id=_student_id_counter, **student.model_dump())
    students_db[_student_id_counter] = new_student
    _student_id_counter += 1
    return new_student


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = students_db.get(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} was not found.",
        )
    return student


@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate):
    if student_id not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} was not found.",
        )

    updated_student = Student(id=student_id, **student.model_dump())
    students_db[student_id] = updated_student
    return updated_student


@router.delete("/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} was not found.",
        )

    del students_db[student_id]
    return {"message": f"Student with id {student_id} was deleted successfully."}
