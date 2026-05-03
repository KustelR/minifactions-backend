class Game:
    active_objects = []

    def register_object(self, obj):
        self.active_objects.append(obj)

    def turn(self):
        for obj in self.active_objects: obj.delta()