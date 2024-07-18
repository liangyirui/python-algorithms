"""
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.
"""

from collections import deque

from binary_tree import TreeNode


def delete_nodes(root: TreeNode | None, to_delete: list[int]) -> list[TreeNode | None]:
    to_delete_set = set(to_delete)
    forest = []
    root = dfs(root, to_delete_set, forest)
    if root:
        forest.append(root)
    return forest


def dfs(
    node: TreeNode | None, to_delete_set: set[int], forest: list[TreeNode | None]
) -> TreeNode | None:
    if node is None:
        return None
    node.left = dfs(node.left, to_delete_set, forest)
    node.right = dfs(node.right, to_delete_set, forest)
    if node.val in to_delete_set:
        if node.left:
            forest.append(node.left)
        if node.right:
            forest.append(node.right)
        return None
    return node


def delete_nodes_bfs(
    root: TreeNode | None, to_delete: list[int]
) -> list[TreeNode | None]:
    forest = []
    if root is None:
        return forest
    to_delete_set = set(to_delete)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            if node.left.val in to_delete_set:
                node.left = None
        if node.right:
            queue.append(node.right)
            if node.right.val in to_delete_set:
                node.right = None
        if node.val in to_delete_set:
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)

    if root.val not in to_delete_set:
        forest.append(root)

    return forest
