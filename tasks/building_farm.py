import random


from Entities import Task
from buildings.Farm import Farm
from tasks.StoredTask import StoredTask

def during_invoke(task: Task):
    task.igrok.stamina -= 0.3
    if (task.faction.building_materials < 2):
        task.interrupt()
        return
    task.faction.building_materials -= 2

def end_invoke(task: Task):
    task.chunk.building = Farm(
        task.chunk,
        task.igrok.tech * 2 + 5 * random.random(),
        task.igrok.building * 1.5 + 5 * random.random()
    )

task = StoredTask(
    "building_farm",
    during_invoke=during_invoke,
    end_invoke=end_invoke,
    duration=3
)