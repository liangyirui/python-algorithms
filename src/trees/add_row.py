"""
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth.
Note that the root node is at depth 1.
The adding rule is:
1. Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
2. cur's original left subtree should be the left subtree of the new left subtree root.
3. cur's original right subtree should be the right subtree of the new right subtree root.
4. If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(node: Optional[TreeNode], val: int, d: int, n: int) -> None:
    if node is None:
        return
    if d == n - 1:
        left = node.left
        node.left = TreeNode(val)
        node.left.left = left
        right = node.right
        node.right = TreeNode(val)
        node.right.right = right
    else:
        insert(node.left, val, d + 1, n)
        insert(node.right, val, d + 1, n)


def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        node = TreeNode(val, left=root)
        return node

    insert(root, val, 1, depth)
    return root