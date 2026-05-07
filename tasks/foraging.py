
import random

from Entities import Task
from tasks.StoredTask import StoredTask


def during_foraging(task: Task):
    task.faction.raw_materials += (task.igrok.tech + task.igrok.stamina * 0.2) * (0.2 + random.random() * 0.2)
    task.faction.building_materials += (task.igrok.building + task.igrok.stamina * 0.2) * (0.7 + random.random() * 0.6)
    task.faction.food += (task.igrok.tech * 0.5 + task.igrok.stamina * 0.3) * (0.3 + random.random() * 0.3)
    task.igrok.stamina -= 1.5 / task.igrok.tech + random.random() * 0.1

task = StoredTask(
    "foraging",
    during_invoke=during_foraging
)
