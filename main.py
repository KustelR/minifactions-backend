from fastapi import FastAPI
from Game import Game
from task_manager import get_tasks

app = FastAPI()


@app.get("/")
def read_root():
    game = Game(1,3)
    tasks = get_tasks()

    faction = game.create_faction("loitsk")
    igrok = game.create_igrok(5, 4, 7, 4, 9)
    chunk = game.grid.at(0,0)
    faction.add_igrok(igrok)
    faction.claim(game.grid.at(0, 0))
    faction.name = "espada"
    igrok.assign(tasks["mining"].task(igrok, chunk, faction, 4))
    game.turn()
    game.turn()
    game.turn()
    game.turn()
    faction.building_materials += 2000
    igrok.assign(tasks["building_fort"].task(igrok, chunk, faction))
    game.turn()
    game.turn()
    game.turn()
    game.turn()
    game.turn()
    game.turn()
    return game.toJSON()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}