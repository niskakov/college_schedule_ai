from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.timetable import Teacher, Preference
from app.schemas.timetable import TeacherCreate, Teacher
from typing import List

router = APIRouter()

@router.post("/", response_model=Teacher)
async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    
    for slot, weight in teacher.preferences.items():
        db_preference = Preference(teacher_id=db_teacher.id, slot=slot, weight=weight)
        db.add(db_preference)
    db.commit()
    
    return db_teacher

@router.get("/", response_model=List[Teacher])
async def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()
  
