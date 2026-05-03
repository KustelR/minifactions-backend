from Entities import Task


class StoredTask:
    start_invoke: callable[Task] | None = None
    during_invoke: callable[Task] | None = None
    end_invoke: callable[Task] | None = None
    def __init__(self, start_invoke: callable[Task], during_invoke: callable[Task], end_invoke: callable[Task]):
        self.start_invoke = start_invoke
        self.during_invoke = during_invoke
        self.end_invoke = end_invoke