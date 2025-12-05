import time


class Day3:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()
        self.freshid = 0
        self.freshtotal = 0
        self.ranges = []

    def load_input(self):
        with open("2025\\3.txt") as fl:
            self.lines = fl.read().strip().split("\n")

    def part_one(self):
        lines = self.lines
        jolt1 = 0

        for line in lines:
            max1 = 0
            bench = 0
            for index in range(0, len(line) - 1):
                if (val := int(line[index])) > bench:
                    bench = val
                    max1 = int(line[index] + max(line[index + 1 :]))

            jolt1 += max1

        return jolt1

    def part_two(self):
        lines = self.lines
        jolt2 = 0

        for line in lines:
            max2 = ""
            start = 0
            temp = 0

            for gap in range(12, 0, -1):
                bench = 0
                work = [
                    int(x)
                    for x in list(
                        line[start : (-gap) + 1] if (-gap) + 1 < 0 else line[start:]
                    )
                ]

                for index in range(0, len(work)):
                    if (val := int(work[index])) > bench:
                        bench = val
                        temp = index + 1

                start += temp
                max2 += str(bench)

            jolt2 += int(max2)

        return jolt2

    def solve(self, quiet=False):
        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day3().solve()

"""
import timeit
print(f"{timeit.timeit("Day3().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs
