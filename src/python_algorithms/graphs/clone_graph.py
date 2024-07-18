"""
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list(list[Node]) of its neighbors.
"""

from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    if node is None:
        return None
    node_copy = Node(node.val)
    marked = [None] * 101
    dfs(node, node_copy, marked)
    return node_copy


def dfs(node: Node | None, node_copy: Node | None, marked: list[Node]) -> None:
    marked[node_copy.val] = node_copy
    for neighbor in node.neighbors:
        if marked[neighbor.val] is None:
            copy = Node(neighbor.val)
            node_copy.neighbors.append(copy)
            dfs(neighbor, copy, marked)
        else:
            node_copy.neighbors.append(marked[neighbor.val])


def bsf(node: Node | None) -> Node | None:
    if node is None:
        return None
    node_map = {}
    node_copy = Node(node.val)
    queue = deque([Node])
    while queue:
        n = queue.popleft()
        for nei in n.neighbors:
            if nei not in node_map:
                nei_copy = Node(nei.val)
                node_map[nei] = nei_copy
                queue.append(nei)
            node_map[n].neighbors.append(node_map[nei])
    return node_copy
