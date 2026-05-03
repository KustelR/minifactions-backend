class Grid:
    test = 1
    chunks = [[]]

    def at(self, x: int, y: int):
        return self.chunks[y][x]
    
    def delta(self):
        for line in self.chunks:
            for chunk in line:
                chunk.delta()

    def __init__(self, height: int, width: int) -> Grid:
        self.chunks = generate_chunks(width, height)


class Chunk:
    owned_by = None
    terrain_type = None


    def __init__(self):
        self.terrain_type = "plains"


    def delta(self):
        pass


def generate_chunks(width: int, height: int):
    result = []
    for y in range(height):
        line = []
        for x in range(width):
            line.append(Chunk())
        result.append(line)

    return result