from collections import deque


class Board:
    def __init__(self):
        self.grid = [
            ["Kitchen", ".", ".", ".", ".", "Library"],
            [".", ".", ".", ".", ".", "."],
            [".", ".", "Hall", ".", ".", "."],
            [".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "."],
            ["Study", ".", ".", ".", ".", "Lounge"]
        ]

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def get_start_position(self):
        return (self.rows // 2, self.cols // 2) 

    def get_neighbors(self, pos):
        r, c = pos
        moves = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

        return [
            (nr, nc)
            for nr, nc in moves
            if 0 <= nr < self.rows and 0 <= nc < self.cols
        ]

    def get_reachable_positions(self, start_pos, steps):
        queue = deque([(start_pos, 0)])
        visited = set([start_pos])
        reachable = set()

        while queue:
            pos, dist = queue.popleft()

            if dist > steps:
                continue

            reachable.add(pos)

            for neighbor in self.get_neighbors(pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return reachable

    def positions_to_rooms(self, positions):
        room_positions = {}

        for r, c in positions:
            value = self.grid[r][c]
            if value != ".":
                room_positions[value] = (r, c)

        return room_positions