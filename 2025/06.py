import time


class Day6:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()

    def load_input(self):
        with open("2025\\06.txt") as fl:
            lines = fl.read().strip().split("\n")
            # print(lines)
            start = -1
            end = -1
            nums = []
            self.operators = lines[-1].split()

            for index in range(z := len(lines[:-1][0])):  # part 2 cooked fr
                gap = True
                for line in lines[:-1]:
                    if line[index] != " ":
                        gap = False
                        break

                if gap is True:
                    start = end + 1
                    end = index
                    nums.append([l[start:end] for l in lines[:-1]])

                elif index + 1 == z:
                    nums.append([l[end + 1 :] for l in lines[:-1]])

            self.lines = nums

    def part_one(self):
        lines = self.lines
        operators = self.operators
        total = 0

        for index, ope in enumerate(operators):
            cache = 0 if ope == "+" else 1

            for val in lines[index]:
                if ope == "+":
                    cache += int(val.strip())
                else:
                    cache *= int(val.strip())

            total += cache

        return total

    def part_two(self):
        lines: list[str] = self.lines
        operators = self.operators
        total = 0

        for index, ope in enumerate(operators):
            cache = 0 if ope == "+" else 1
            work = lines[index]

            for place in range(-1, -(len(work[0]) + 1), -1):
                if ope == "+":
                    cache += int("".join([m[place] for m in work]))
                else:
                    cache *= int("".join([m[place] for m in work]))

            total += cache

        return total

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
