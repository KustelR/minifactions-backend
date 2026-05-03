from fastapi import FastAPI
from Grid import Grid
from Faction import Faction

app = FastAPI()


@app.get("/")
def read_root():
    grid = Grid(100, 100)
    faction = Faction("loitsk")
    faction.claim(grid.at(0, 0))
    faction.name = "espada"
    return grid


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}