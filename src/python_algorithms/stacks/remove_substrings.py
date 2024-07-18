"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.
Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
"""


def maximum_gain(s: str, x: int, y: int) -> int:
    a, b = "ab", "ba"
    if x < y:
        x, y = y, x
        a, b = b, a
    s_first = remove_substring(s, a)
    s_second = remove_substring(s_first, b)
    score = (len(s) - len(s_first)) // 2 * x + (len(s_first) - len(s_second)) // 2 * y
    return score


def remove_substring(s: str, target: str) -> str:
    stack = []
    for ch in s:
        if ch == target[1] and stack and stack[-1] == target[0]:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


if __name__ == "__main__":
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    print(maximum_gain(s, x, y))
