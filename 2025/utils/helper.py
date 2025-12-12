# Helper functions


# for binary tree storing and swapping

def push_max(heap, node):
    heap.append(node)
    pos = len(heap) - 1
    while pos > 0:
        par = (pos - 1) // 2
        if heap[pos][0] <= heap[par][0]:
            break
        heap[pos], heap[par] = heap[par], heap[pos]
        pos = par

def replace_root_and_sift_down(heap, node):
    heap[0] = node
    pos = 0
    n = len(heap)
    while True:
        l = 2 * pos + 1
        r = 2 * pos + 2
        largest = pos
        if l < n and heap[l][0] > heap[largest][0]:
            largest = l
        if r < n and heap[r][0] > heap[largest][0]:
            largest = r
        if largest == pos:
            break
        heap[pos], heap[largest] = heap[largest], heap[pos]
        pos = largest


class DSU: 
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n   # size of each component

    def find(self, x):
        while self.parent[x] != x: 
            # path halving (faster than naive)
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # already same group

        # attach smaller tree under larger one
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
