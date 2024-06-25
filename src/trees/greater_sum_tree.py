"""
Given the root of a BST, convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in the BST.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def bst_to_gst(root: Optional[TreeNode]) -> Optional[TreeNode]:
    node_sum = [0]
    dfs(root, node_sum)
    return root


def dfs(node: Optional[TreeNode], node_sum: list[int]) -> None:
    if node is None:
        return
    dfs(node.right, node_sum)
    node_sum[0] += node.val
    node.val = node_sum[0]
    dfs(node.left, node_sum)


def bst_to_gst_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    node_sum = 0
    stack = []
    node = root
    while stack or node:

        while node:
            stack.append(node)
            node = node.right
        
        node = stack.pop()
        node_sum += node.val
        node.val = node_sum

        node = node.left
    return root