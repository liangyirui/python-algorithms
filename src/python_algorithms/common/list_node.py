from typing import Self


class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None) -> None:
        self.val = val
        self.next = next


def list_to_linked_list(arr: list[int]) -> ListNode | None:
    sentinel = curr = ListNode()
    for val in arr:
        node = ListNode(val)
        curr.next = node
        curr = curr.next
    return sentinel.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
