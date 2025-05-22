from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.timetable import Course, Preference, Room, Schedule
from app.schemas.timetable import TimetableResponse
from app.ai.timetable_generator import generate_timetable

router = APIRouter()

@router.post("/generate", response_model=TimetableResponse)
async def generate_timetable_endpoint(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    preferences = db.query(Preference).all()
    rooms = db.query(Room).all()
    
    timetable = generate_timetable(courses, preferences, rooms)
    
    # Очистка старого расписания
    db.query(Schedule).delete()
    
    # Сохранение нового расписания
    for gene in timetable:
        schedule = Schedule(
            course_id=gene["course_id"],
            day=gene["day"],
            slot=gene["slot"],
            room_id=gene["room_id"]
        )
        db.add(schedule)
    db.commit()
    
    schedules = db.query(Schedule).all()
    return {"schedules": schedules}
  
