"""
Give the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
"""

from collections import defaultdict, deque

from binary_tree import TreeNode


def vertical_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    queue = deque([(root, 0)])
    node_col = defaultdict(list)
    min_col = max_col = 0
    while queue:
        node, col = queue.popleft()
        node_col[col].append(node.val)
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    return [node_col[x] for x in range(min_col, max_col + 1)]
