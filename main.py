import json

from fastapi import FastAPI
from Entities import Faction, Task, Igrok, Chunk
from Game import Game

app = FastAPI()

def start_gather_wood(task: Task):
    print(task.chunk.to_dict())
    task.chunk.affected_by.append(task)
    pass


def end_gather_wood(task: Task):
    task.igrok.task = None
    task.chunk.affected_by = None
    task.chunk.igroks

def during_gather_wood(task: Task):
    task.faction.raw_materias += task.igrok.tech
    task.igrok.stamina -= 1


@app.get("/")
def read_root():
    game = Game(1,3)


    faction = game.create_faction("loitsk")
    igrok = game.create_igrok(5, 4, 7, 4, 9)
    faction.add_igrok(igrok)
    igrok.assign(Task(igrok, game.grid.at(1,0), faction, 10, start_gather_wood, during_gather_wood, end_gather_wood))
    faction.claim(game.grid.at(0, 0))
    faction.name = "espada"
    game.turn()
    return game.toJSON()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}