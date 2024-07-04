"""
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
Return the head of the modified linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def merge_nodes(head: ListNode | None) -> ListNode | None:
    slow = fast = head.next
    while fast:
        node_sum = 0
        while fast.val != 0:
            node_sum += fast.val
            fast = fast.next
        slow.val = node_sum
        fast = fast.next
        slow.next = fast
        slow = slow.next
    return head.next
