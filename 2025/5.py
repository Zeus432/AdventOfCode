import time


class Day5:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()
        self.freshid = 0
        self.freshtotal = 0
        self.ranges = []
        self.ids = sorted([int(x) for x in self.lines[1]])

    def load_input(self):
        with open("2025\\5.txt") as fl:
            self.lines = [i.split("\n") for i in fl.read().strip().split("\n\n")]

    def resolve_ranges(self):
        for start, end in sorted(
            [[int(k) for k in j.split("-")] for j in self.lines[0]]
        ):

            if len(self.ranges) == 0:
                self.ranges.append([start, end])
                continue

            if start <= self.ranges[-1][1]:
                if end <= self.ranges[-1][1]:
                    continue

                else:
                    self.ranges[-1][1] = end

            else:
                self.ranges.append([start, end])

    def part_one(self):
        step = 0
        limit = len(self.ranges)
        for item in self.ids:
            while item > self.ranges[step][1] and step != limit - 1:
                step += 1

            start, end = self.ranges[step]

            if item >= start and item <= end:
                self.freshid += 1

        return self.freshid

    def part_two(self):
        for start, end in self.ranges:
            self.freshtotal += end + 1 - start

        return self.freshtotal

    def solve(self, quiet=False):
        self.resolve_ranges()

        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day5().solve()

"""
import timeit
print(f"{timeit.timeit("Day5().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs
