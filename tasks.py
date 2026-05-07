import random

from Entities import Chunk, Faction, Igrok, Task


class StoredTask:
    name: str
    start_invoke: callable[Task] | None = None
    during_invoke: callable[Task] | None = None
    end_invoke: callable[Task] | None = None
    def __init__(self, name: str, 
                 start_invoke: callable[Task] | None = None, 
                 during_invoke: callable[Task] | None = None, 
                 end_invoke: callable[Task] | None = None):
        self.name = name
        self.start_invoke = start_invoke
        self.during_invoke = during_invoke
        self.end_invoke = end_invoke

    def task(self, igrok: Igrok, chunk: Chunk, faction: Faction, duration: int):
        return Task(self.name, igrok, chunk, faction, duration, self.start_invoke, self.during_invoke, self.end_invoke)


def during_foraging(task: Task):
    task.faction.raw_materials += (task.igrok.tech + task.igrok.stamina * 0.2) * (0.7 + random.random() * 0.6)
    task.faction.food += (task.igrok.tech * 0.5 + task.igrok.stamina * 0.3) * (0.3 + random.random() * 0.3)
    task.igrok.stamina -= 1.5 / task.igrok.tech + random.random() * 0.1

    
foraging = StoredTask(
    "foraging",
    during_invoke=during_foraging
)

def get_tasks():
    result: list[StoredTask] = [
        foraging
    ]

    return result
