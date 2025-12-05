import time


class Day6:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()
    
    def load_input(self):
        with open("2025\\06.txt") as fl:
            self.lines = fl.read().strip().split("\n")
    
    def part_one(self):
        return 0

    def part_two(self):
        return 0
    
    def solve(self, quiet=False):
        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day6().solve()

"""
import timeit
print(f"{timeit.timeit("Day6().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs