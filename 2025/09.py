import time
from itertools import combinations


class Day9:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()

    def load_input(self):
        with open("2025\\09.txt") as fl:
            self.lines = sorted(
                [
                    list(map(lambda n: int(n), coords.split(",")))
                    for coords in fl.read().strip().split("\n")
                ]
            )

    def part_one(self):
        lines = self.lines
        marea = 0

        for (x1, y1), (x2, y2) in combinations(lines, 2):
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            if area > marea:
                marea = area

        return marea

    def part_two(self):
        lines = self.lines
        return 0

    def solve(self, quiet=False):
        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day9().solve()

"""
import timeit
print(f"{timeit.timeit("Day9().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs
