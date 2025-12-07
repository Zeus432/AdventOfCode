import time


class Day7:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()

    def load_input(self):
        with open("2025\\07.txt") as fl:
            self.lines = [list(a) for a in fl.read().strip().split("\n")]

    def part_one_and_two(self):
        lines = self.lines
        beams = {lines[0].index("S"): 1}
        split = 0

        for line in lines[1:]:
            beam_copy = [(x, y) for x, y in beams.items()]
            for pos, val in beam_copy:
                if line[pos] == ".":
                    line[pos] = "|" # just for visuals no impact if removed

                elif line[pos] == "^":
                    split += 1
                    if (pos - 1) in beams:
                        beams[pos - 1] += val
                    else:
                        beams[pos - 1] = val

                    if (pos + 1) in beams:
                        beams[pos + 1] += val
                    else:
                        beams[pos + 1] = val

                    beams.pop(pos)

        return split, sum(beams.values())

    def solve(self, quiet=False):
        solution = self.part_one_and_two()

        if not quiet:
            print("Part 1:", solution[0])
            print("Part 2:", solution[1])
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day7().solve()

"""
import timeit
print(f"{timeit.timeit("Day7().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs
