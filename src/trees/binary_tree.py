from typing import Self


class TreeNode:
    def __init__(
        self, val: int = 0, left: Self | None = None, right: Self | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"
