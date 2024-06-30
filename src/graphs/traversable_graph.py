"""
Alice and Bob have an undirected graph of n nodes and three types of edges:
Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidrectional edge of type typei between node ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
"""


class UF:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def find(self, p: int) -> int:
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        p, q = self.find(p), self.find(q)
        if p == q:
            return False
        if self.size[q] > self.size[p]:
            self.parent[p] = q
            self.size[q] += self.size[p]
        else:
            self.parent[q] = p
            self.size[p] += self.size[q]
        self.components -= 1
        return True


def max_num_edges_to_remove(n: int, edges: list[list[int]]) -> int:
    alice = UF(n + 1)
    bob = UF(n + 1)
    edges_to_remove = 0
    for tp, v, w in edges:
        if tp == 3:
            edges_to_remove += 1 - (alice.union(v, w) and bob.union(v, w))
    for tp, v, w in edges:
        if tp == 1:
            edges_to_remove += 1 - alice.union(v, w)
        if tp == 2:
            edges_to_remove += 1 - bob.union(v, w)
    if alice.components != 2 or bob.components != 2:
        return -1
    return edges_to_remove


if __name__ == "__main__":
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]
    print(max_num_edges_to_remove(n, edges))
