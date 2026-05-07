import json

from Entities import Chunk


class Grid:
    chunks: list[list[Chunk]] = [[]]
    current = 0

    def at(self, x: int, y: int):
        return self.chunks[y][x]
    
    def delta(self):
        for line in self.chunks:
            for chunk in line:
                chunk.delta()

    def __init__(self, height: int, width: int) -> Grid:
        self.chunks = generate_chunks(width, height)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= len(self.chunks):
            raise StopIteration()
        tgt = list(map(lambda chunk: chunk.to_dict(), self.chunks[self.current]))
        self.current += 1
        return tgt


def generate_chunks(width: int, height: int):
    result = []
    for y in range(height):
        line = []
        for x in range(width):
            line.append(Chunk((x, y)))
        result.append(line)

    return result