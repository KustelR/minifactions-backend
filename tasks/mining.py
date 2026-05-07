
import random

from Entities import Task
from tasks.StoredTask import StoredTask


def during_mining(task: Task):
    task.faction.emeralds += max(0, random.randint(0, 100) - 95)
    task.faction.raw_materials += (task.igrok.tech + task.igrok.stamina * 0.2) * (2 + random.random())
    task.faction.building_materials += (task.igrok.building + task.igrok.stamina * 0.2) * (0.2 + random.random() * 0.6)

    if task.chunk.terrain_type == "mountain":
        task.faction.raw_materials += 10
        task.faction.emeralds + 5



task = StoredTask(
    "mining",
    during_invoke=during_mining
)