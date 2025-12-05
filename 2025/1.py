import time


class Day1:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()
        self.start = 50

    def load_input(self):
        with open("2025\\1.txt") as fl:
            self.lines = [[i[0], int(i[1:])] for i in fl.read().strip().split("\n")]

    def solve(self, start=50, quiet=False):
        lines = self.lines
        count1 = 0
        count2 = 0
        num = start

        for direction, val in lines:
            if direction == "R":
                count2 += (num + val) // 100
                num = (num + val) % 100

            else:
                if num == 0:
                    count2 += val // 100

                else:
                    if val >= num:
                        count2 += 1 + (val - num) // 100

                num = (num - val) % 100

            if num == 0:
                count1 += 1

        if not quiet:
            print("Part 1:", count1)
            print("Part 2:", count2)
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day1().solve()

"""
import timeit
print(f"{timeit.timeit("Day1().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs
