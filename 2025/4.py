class Forklift:
    def __init__(self, lines: list, cycles: int = 1):
        self.lines = lines
        self.cycles = cycles
        self.limits = [len(lines[0]), len(lines)]
        self.accessible = 0
        self.overall = 0

    def check_surroundings(self, x, y):
        counter = 0
        surr_coords = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]

        for b, a in surr_coords:
            if (
                x + a >= 0
                and x + a < self.limits[0]
                and y + b >= 0
                and y + b < self.limits[1]
            ):
                if self.lines[y + b][x + a] in ["@", "x"]:
                    counter += 1

        if counter < 4:
            self.lines[y][x] = "x"
            self.accessible += 1

    def clean_grid(self):
        for y, line in enumerate(self.lines):
            for x, roll in enumerate(line):
                if roll == "x":
                    self.lines[y][x] = "."

        self.accessible = 0

    def part_one(self):
        for y, line in enumerate(self.lines):
            for x, roll in enumerate(line):
                if roll == "@":
                    self.check_surroundings(x, y)

        return self.accessible

    def part_two(self):
        while (removed := self.part_one()) > 0:
            self.overall += removed
            self.clean_grid()

        return self.overall


with open("2025\\4.txt") as fl:
    lines = [list(i) for i in fl.read().strip().split("\n")]

grid = Forklift(lines)
part1, part2 = grid.part_one(), grid.part_two()
print("Part 1:", part1)
print("Part 2:", part2)
