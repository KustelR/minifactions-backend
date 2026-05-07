from Entities import Chunk, Faction, Igrok, Task


class StoredTask:
    name: str
    start_invoke: callable[Task] | None = None
    during_invoke: callable[Task] | None = None
    end_invoke: callable[Task] | None = None
    duration: int | None
    def __init__(self, name: str, 
                 start_invoke: callable[Task] | None = None, 
                 during_invoke: callable[Task] | None = None, 
                 end_invoke: callable[Task] | None = None,
                 duration: int | None = None):
        self.name = name
        self.start_invoke = start_invoke
        self.during_invoke = during_invoke
        self.end_invoke = end_invoke
        self.duration = duration

    def task(self, igrok: Igrok, chunk: Chunk, faction: Faction, duration: int | None = None):
        return Task(
            self.name, 
            igrok,
            chunk,
            faction,
            self.duration if self.duration else duration if duration else 1,
            self.start_invoke,
            self.during_invoke,
            self.end_invoke)
