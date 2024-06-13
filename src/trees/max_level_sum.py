from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum_dfs(root: Optional[TreeNode]) -> int:
    level_sum = []

    def dfs(node, level):
        if node is None:
            return
        if len(level_sum) == level:
            level_sum.append(node.val)
        else:
            level_sum[level] += node.val
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    max_level, max_sum = 0, float('-inf')
    for i, val in enumerate(level_sum):
        if val > max_sum:
            max_level = i
            max_sum = val
    return max_level


def max_level_sum_bfs(root: Optional[TreeNode]) -> int:
    if root is None:
        return -1
    queue = deque([root])
    max_level, max_sum = 0, float('-inf')
    level = 0
    while queue:
        size = len(queue)
        level_sum = 0
        level += 1
        for _ in range(size):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
    return max_level