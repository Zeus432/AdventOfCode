import time
from utils.helper import push_max, replace_root_and_sift_down, DSU


class Day8:
    def __init__(self):
        self._start = time.perf_counter()
        self.load_input()
        self.initialize()
    
    def load_input(self):
        with open("2025\\08.txt") as fl:
            self.lines = [list(map(lambda n: int(n), coords.split(","))) for coords in fl.read().strip().split("\n")]
    
    def initialize(self):
        lines = self.lines
        n = len(lines)
        heap = []

        for i in range(n-1):
            x1, y1, z1 = lines[i]
            for j in range(i+1, n):
                x2, y2, z2 = lines[j]
                d = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 

                heap.append((d, i, j))
        
        heap = sorted(heap, key = lambda x: x[0])
        self.heap = heap
    
    def part_one(self, k = 1000):
        lines = self.lines
        n = len(lines)
        heap = self.heap[:k]
        dsu = DSU(n)

        for d, i, j in heap:
            dsu.union(i, j)

        sizes = []
        for x in range(n):
            if dsu.parent[x] == x:
                sizes.append(dsu.size[x])
        
        sizes.sort(reverse=True)
        return sizes[0] * sizes[1] * sizes[2]
    
    def part_two(self):
        lines = self.lines
        n = len(lines)
        heap = self.heap
        dsu = DSU(n)
        last = None

        for d, i, j in heap:
            merged = dsu.union(i, j)
            if merged:
                n -= 1
                last = (i, j)
                if n == 1:
                    break

        if last is None:
            raise RuntimeError("No merging occurred — unexpected input")

        return lines[last[0]][0] * lines[last[1]][0]
    
    def solve(self, quiet=False):
        if not quiet:
            print("Part 1:", self.part_one())
            print("Part 2:", self.part_two())
            print(f"Runtime: {(time.perf_counter() - self._start) * 1000:.3f} ms")


Day8().solve()

"""
import timeit
print(f"{timeit.timeit("Day8().solve(quiet=True)", globals=globals(), number=1000):.3f} ms per run")
"""  # Average runtime over 1000 runs