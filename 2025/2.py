import time
import math


class Day2:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()
        self.powers = [10 ** (l) for l in range(len(str(self.lines[-1][1])) + 1)]

    def load_input(self):
        with open("2025\\2.txt") as fl:
            self.lines = sorted(
                [[int(j) for j in i.split("-")] for i in fl.read().strip().split(",")]
            )

    def part_one(self):
        lines = self.lines
        powers = self.powers
        invalid1 = set()

        for start, end in lines:
            minm = len(str(start))
            maxm = len(str(end))
            split = 2

            for length in range(math.ceil(minm / split), (maxm // split) + 1):
                multi = sum(powers[: split * length : length])
                base = powers[length - 1]
                top = powers[length] - 1

                sta = max(base, (start + multi - 1) // multi)
                stp = min(top, end // multi)

                if sta <= stp:
                    invalid1.update((n * multi for n in range(sta, stp + 1)))

        return sum(invalid1)

    def part_two(self):
        lines = self.lines
        powers = self.powers
        invalid2 = set()

        for start, end in lines:
            minm = len(str(start))
            maxm = len(str(end))

            for split in range(2, maxm + 1):
                for length in range(math.ceil(minm / split), (maxm // split) + 1):
                    multi = sum(powers[: split * length : length])
                    base = powers[length - 1]
                    num = base * multi

                    multi = sum(powers[: split * length : length])
                    base = powers[length - 1]
                    top = powers[length] - 1

                    sta = max(base, (start + multi - 1) // multi)
                    stp = min(top, end // multi)

                    if sta <= stp:
                        invalid2.update((n * multi for n in range(sta, stp + 1)))

        return sum(invalid2)

    def solve(self, quiet=False):
        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day2().solve()

"""
import timeit
print(f"{timeit.timeit("Day2().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs
