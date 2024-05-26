"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    frequencies = defaultdict(int)
    curr_sum = 0
    count = 0
    for num in nums:
        curr_sum += num
        if curr_sum == k:
            count += 1
        if curr_sum - k in frequencies:
            count += frequencies[curr_sum - k]
        frequencies[curr_sum] += 1
    return count


def main() -> None:
    nums = [1, 2, 3]
    k = 3
    count = subarray_sum(nums, k)
    print(f"There are {count} subarrays whose sum equals k")


if __name__ == "__main__":
    main()