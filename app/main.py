from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import timetable, teachers, groups, rooms
from app.db.database import engine
from app.models import base
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="College Schedule AI")

# Настройка CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение маршрутов
app.include_router(timetable.router, prefix="/timetable", tags=["timetable"])
app.include_router(teachers.router, prefix="/teachers", tags=["teachers"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])

# Создание таблиц в базе данных
base.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "College Schedule AI API"}
  
