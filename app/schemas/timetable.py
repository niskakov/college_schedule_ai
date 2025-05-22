from pydantic import BaseModel
from typing import List, Dict

class TeacherBase(BaseModel):
    name: str

class TeacherCreate(TeacherBase):
    preferences: Dict[int, int]  # {slot: weight}

class Teacher(TeacherBase):
    id: int
    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    class Config:
        orm_mode = True

class RoomBase(BaseModel):
    name: str

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: int
    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    name: str
    teacher_id: int
    group_id: int
    duration: int = 1

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    class Config:
        orm_mode = True

class ScheduleBase(BaseModel):
    course_id: int
    day: str
    slot: int
    room_id: int

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id: int
    class Config:
        orm_mode = True

class TimetableResponse(BaseModel):
    schedules: List[Schedule]
  
