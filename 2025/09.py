import time
from itertools import combinations
from collections import deque


class Day9:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()

    def load_input(self):
        with open("2025\\09.txt") as fl:
            self.lines = [
                tuple(map(int, line.split(",")))
                for line in fl.read().strip().split("\n")
            ]

    def part_one(self):
        lines = self.lines
        best = 0

        for (x1, y1), (x2, y2) in combinations(lines, 2):
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            if area > best:
                best = area

        return best

    def part_two(self):
        lines = self.lines
        # print(lines)
        n = len(lines)

        # 1. Coordinate compression (tile-aware)

        xs, ys = set(), set()
        # IMPORTANT: include x and x+1, y and y+1 (tiles are unit squares)
        for x, y in lines:
            xs.add(x)
            xs.add(x + 1)
            ys.add(y)
            ys.add(y + 1)

        xs = sorted(xs)
        ys = sorted(ys)

        x_id = {x: i for i, x in enumerate(xs)}
        y_id = {y: i for i, y in enumerate(ys)}

        # print("Original X values:", sorted({x for x, y in boundary}))
        # print("Compressed X grid:", xs)
        # print("X mapping:", x_id)

        # print("Original Y values:", sorted({y for x, y in boundary}))
        # print("Compressed Y grid:", ys)
        # print("Y mapping:", y_id)

        W = len(xs) - 1
        H = len(ys) - 1

        # 2. Rasterize polygon boundary into compressed grid

        grid = [[0] * W for _ in range(H)]  # 0 = unknown

        # Rasterize polygon edges into grid (BOUNDARY = 1)
        for i in range(n):
            x1, y1 = lines[i]
            x2, y2 = lines[(i + 1) % n]

            cx1, cy1 = x_id[x1], y_id[y1]
            cx2, cy2 = x_id[x2], y_id[y2]

            if cx1 == cx2:  # vertical edge
                for cy in range(min(cy1, cy2), max(cy1, cy2)):
                    grid[cy][cx1] = 1
            else:  # horizontal edge
                for cx in range(min(cx1, cx2), max(cx1, cx2)):
                    grid[cy1][cx] = 1

        # 3. Flood fill OUTSIDE from grid border

        # Mark outside as -1
        q = deque()

        # Push all border cells that are not boundary
        for x in range(W):
            if grid[0][x] == 0:
                grid[0][x] = -1
                q.append((x, 0))

            if grid[H - 1][x] == 0:
                grid[H - 1][x] = -1
                q.append((x, H - 1))

        for y in range(H):
            if grid[y][0] == 0:
                grid[y][0] = -1
                q.append((0, y))

            if grid[y][W - 1] == 0:
                grid[y][W - 1] = -1
                q.append((W - 1, y))

        # Flood fill outside
        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] == 0:
                    grid[ny][nx] = -1
                    q.append((nx, ny))

        for y in range(H):
            for x in range(W):
                if grid[y][x] == 0:
                    grid[y][x] = 2  # interior

        # 4. Prefix sums for forbidden tiles (outside = -1)

        bad = [[1 if grid[y][x] == -1 else 0 for x in range(W)] for y in range(H)]

        row_psum = [[0] * (W + 1) for _ in range(H)]

        for y in range(H):
            for x in range(W):
                row_psum[y][x + 1] = row_psum[y][x] + bad[y][x]

        # Tile widths
        xw = [0] * (W + 1)
        for i in range(W):
            xw[i + 1] = xw[i] + (xs[i + 1] - xs[i])

        yw = [0] * (H + 1)
        for i in range(H):
            yw[i + 1] = yw[i] + (ys[i + 1] - ys[i])

        # 5. Try all red-point rectangles

        redtiles = [(x_id[x], y_id[y]) for (x, y) in lines]
        best = 0

        for (x1, y1), (x2, y2) in combinations(redtiles, 2):
            if x1 == x2 or y1 == y2:
                continue  # must be opposite corners

            lx = min(x1, x2)
            rx = max(x1, x2) + 1

            ty = min(y1, y2)
            by = max(y1, y2) + 1

            width = xw[rx] - xw[lx]
            height = yw[by] - yw[ty]
            area = width * height

            if area <= best:
                continue

            for y in range(ty, by):
                if row_psum[y][rx] - row_psum[y][lx] > 0:
                    break

            else:
                best = area

        return best

    def print_grid_filled(self, grid):  # for checking visually
        for row in reversed(grid):
            print("".join("#" if c == 1 else "I" if c == 2 else "." for c in row))

    def solve(self, quiet=False):
        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day9().solve()


import timeit

print(
    f"{timeit.timeit("Day9().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run"
)
# Average runtime over 1000 runs
