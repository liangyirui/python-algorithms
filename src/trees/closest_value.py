"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
If there are multiple answers, print the smallest.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closest_value(root: Optional[TreeNode], target: float) -> int:
    node = root
    closest = node.val
    while node:
        if abs(node.val - target) < abs(closest - target):
            closest = node.val
        elif abs(node.val - target) == abs(closest - target):
            closest = min(closest, node.val)
        node = node.left if node.val > target else node.right
    return closest