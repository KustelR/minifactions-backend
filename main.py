from fastapi import FastAPI
from Game import Game
from tasks import get_tasks

app = FastAPI()


@app.get("/")
def read_root():
    game = Game(1,3)
    tasks = get_tasks()

    faction = game.create_faction("loitsk")
    igrok = game.create_igrok(5, 4, 7, 4, 9)
    igrok.assign(tasks[0].task(igrok, game.grid.at(0,0), faction, 2))
    faction.add_igrok(igrok)
    faction.claim(game.grid.at(0, 0))
    faction.name = "espada"
    game.turn()
    game.turn()
    game.turn()
    game.turn()
    game.turn()
    return game.toJSON()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}