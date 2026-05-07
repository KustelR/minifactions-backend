import random

from Entities import Task
from tasks.StoredTask import StoredTask
from buildings.Fortification import Fortification


def during_invoke(task: Task):
    task.igrok.stamina -= 0.3
    if (task.faction.building_materials < 12):
        task.interrupt()
        return
    task.faction.building_materials -= 12

def end_invoke(task: Task):
    task.chunk.building = Fortification(
        task.chunk,
        task.igrok.tech * 2 + 5 * random.random(),
        task.igrok.building * 1.5 + 5 * random.random()
    )

task = StoredTask(
    "building_fort",
    during_invoke=during_invoke,
    end_invoke=end_invoke,
    duration=5
)