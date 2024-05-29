"""
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.
"""

def num_steps(s: str) -> int:
    n = len(s)
    carry = 0
    steps = 0
    for i in range(n - 1, 0, -1):
        num = ord(s[i]) - ord('0') + carry
        if num % 2 == 1:
            steps += 2
            carry = 1
        else:
            steps += 1
    return steps + carry


def main():
    s = "1101"
    num = num_steps(s)
    print(num)


if __name__ == "__main__":
    main()
