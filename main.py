class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True


def solve(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    n, k, bucket_cost, bond_cost = map(int, lines[0].split())
    edges = []

    for i in range(1, n + 1):
        edges.append((bucket_cost, 0, i))

    for line in lines[1:]:
        u, v = map(int, line.split())
        edges.append((bond_cost, u, v))

    edges.sort()
    uf = UnionFind(n)
    total_cost = 0

    for cost, u, v in edges:
        if uf.union(u, v):
            total_cost += cost

    print("Minimum total cost:", total_cost)


if __name__ == "__main__":
    import os
    path = input("Enter absolute path of input file: ").strip()
    if not os.path.isfile(path):
        print("Invalid path.")
    else:
        solve(path)
