from fastapi import FastAPI
from Entities import Faction
from Game import Game

app = FastAPI()


@app.get("/")
def read_root():
    game = Game(10,10)
    faction = game.create_faction("loitsk")
    faction.claim(game.grid.at(0, 0))
    faction.name = "espada"
    return game


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}