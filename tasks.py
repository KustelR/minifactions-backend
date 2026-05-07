from Entities import Chunk, Faction, Igrok, Task


class StoredTask:
    start_invoke: callable[Task] | None = None
    during_invoke: callable[Task] | None = None
    end_invoke: callable[Task] | None = None
    def __init__(self, start_invoke: callable[Task], during_invoke: callable[Task], end_invoke: callable[Task]):
        self.start_invoke = start_invoke
        self.during_invoke = during_invoke
        self.end_invoke = end_invoke

    def task(this, igrok: Igrok, chunk: Chunk, faction: Faction, duration: int):
        return Task(igrok, chunk, faction, duration, this.start_invoke, this.during_invoke, this.end_invoke)