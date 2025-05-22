import random
import numpy as np
from deap import base, creator, tools, algorithms
from app.models.timetable import Course, Preference
from typing import List

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
SLOTS = [1, 2, 3, 4, 5, 6]

def generate_timetable(courses: List[Course], preferences: List[Preference], rooms: List):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    # Преобразование предпочтений в словарь
    teacher_prefs = {}
    for pref in preferences:
        if pref.teacher_id not in teacher_prefs:
            teacher_prefs[pref.teacher_id] = {}
        teacher_prefs[pref.teacher_id][pref.slot] = pref.weight
    
    def init_individual():
        return creator.Individual([
            {"course_id": course.id, "day": random.choice(DAYS), "slot": random.choice(SLOTS), "room_id": random.choice([r.id for r in rooms])}
            for course in courses
        ])
    
    def evaluate(individual):
        conflicts = 0
        preference_score = 0
        for i, class1 in enumerate(individual):
            for j, class2 in enumerate(individual):
                if i < j and class1["day"] == class2["day"] and class1["slot"] == class2["slot"]:
                    if class1["room_id"] == class2["room_id"]:
                        conflicts += 1
                    course1 = next(c for c in courses if c.id == class1["course_id"])
                    course2 = next(c for c in courses if c.id == class2["course_id"])
                    if course1.teacher_id == course2.teacher_id:
                        conflicts += 1
                    if course1.group_id == course2.group_id:
                        conflicts += 1
            course = next(c for c in courses if c.id == class1["course_id"])
            preference_score += teacher_prefs.get(course.teacher_id, {}).get(class1["slot"], 1)
        return conflicts * 100 - preference_score,
    
    def mutate_individual(individual):
        for gene in individual:
            if random.random() < 0.2:
                gene["day"] = random.choice(DAYS)
                gene["slot"] = random.choice(SLOTS)
                gene["room_id"] = random.choice([r.id for r in rooms])
        return individual,
    
    toolbox = base.Toolbox()
    toolbox.register("individual", init_individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutate_individual)
    toolbox.register("select", tools.selTournament, tournsize=3)
    
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.3, ngen=50, halloffame=hof, verbose=False)
    
    return hof[0]
  
