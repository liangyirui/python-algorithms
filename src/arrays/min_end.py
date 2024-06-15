"""
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation of all elements of nums is x.
Return the minimum possible value of nums[n - 1].
"""

def min_end(n: int, x: int) -> int:
    bit_x = bit_n = 1
    while bit_n < n:
        if (bit_x & x) == 0:
            if bit_n & (n - 1):
                x += bit_x
            bit_n <<= 1
        bit_x <<= 1
    return x



if __name__ == "__main__":
    n = 2
    x = 7
    print(min_end(n, x))