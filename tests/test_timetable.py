import pytest
from app.ai.timetable_generator import generate_timetable
from app.models.timetable import Course, Preference, Room

def test_generate_timetable():
    courses = [
        Course(id=1, name="C1", teacher_id=1, group_id=1, duration=1),
        Course(id=2, name="C2", teacher_id=2, group_id=2, duration=1),
    ]
    preferences = [
        Preference(teacher_id=1, slot=1, weight=10),
        Preference(teacher_id=2, slot=2, weight=10),
    ]
    rooms = [Room(id=1, name="R1"), Room(id=2, name="R2")]
    
    timetable = generate_timetable(courses, preferences, rooms)
    
    assert len(timetable) == len(courses)
    for gene in timetable:
        assert gene["day"] in ["Mon", "Tue", "Wed", "Thu", "Fri"]
        assert gene["slot"] in [1, 2, 3, 4, 5, 6]
        assert gene["room_id"] in [r.id for r in rooms]
      
