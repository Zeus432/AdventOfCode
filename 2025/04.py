import time


class Day4:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()
        self.limits = [len(self.lines[0]), len(self.lines)]
        self.overall = 0
        self.surr_coords = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]

    def load_input(self):
        with open("2025\\04.txt") as fl:
            self.lines = [list(i) for i in fl.read().strip().split("\n")]

    def check_surroundings(self, x, y):
        counter = 0
        limits = self.limits
        surr_coords = self.surr_coords

        for b, a in surr_coords:
            if x + a >= 0 and x + a < limits[0] and y + b >= 0 and y + b < limits[1]:
                if self.lines[y + b][x + a] == "@":
                    counter += 1

                    if counter > 3:
                        return False

        return True

    def clean_grid(self):
        for y, line in enumerate(self.lines):
            for x, roll in enumerate(line):
                if roll == "x":
                    self.lines[y][x] = "."

    def part_one(self):
        lines = self.lines
        to_remove = []
        for y, line in enumerate(lines):
            for x, roll in enumerate(line):
                if roll == "@" and self.check_surroundings(x, y):
                    to_remove.append((x, y))

        for x, y in to_remove:
            lines[y][x] = "x"

        self.overall += len(to_remove)
        return len(to_remove)

    def part_two(self):
        overall = self.overall
        while (removed := self.part_one()) > 0:
            overall += removed
            # print(removed)
            self.clean_grid()

        return overall

    def solve(self, quiet=False):
        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day4().solve()

"""
import timeit
print(f"{timeit.timeit("Day4().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs
