"""
A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
"""

from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None) -> None:
        self.val = val
        self.next = next


def nodes_between_critical_points(head: ListNode | None) -> list[int]:
    min_max_dist = [-1, -1]
    min_dist = float("inf")
    prev, curr = head, head.next
    idx = 1
    prev_critical_idx = first_critical_idx = 0
    while curr.next:
        if (curr.val < prev.val and curr.val < curr.next.val) or (
            curr.val > prev.val and curr.val > curr.next.val
        ):
            if first_critical_idx == 0:
                prev_critical_idx = idx
                first_critical_idx = idx
            else:
                min_dist = min(min_dist, idx - prev_critical_idx)
                prev_critical_idx = idx
        idx += 1
        prev = curr
        curr = curr.next
    if min_dist != float("inf"):
        max_dist = prev_critical_idx - first_critical_idx
        min_max_dist = [min_dist, max_dist]
    return min_max_dist
