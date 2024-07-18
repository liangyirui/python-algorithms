"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.
"""


def subarray_div_by_k(nums: list[int], k: int) -> int:
    remainder = [0] * k
    remainder[0] = 1
    prefix = 0
    count = 0
    for num in nums:
        prefix = (prefix + num) % k
        count += remainder[prefix]
        remainder[prefix] += 1
    return count


def main():
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(subarray_div_by_k(nums, k))


if __name__ == "__main__":
    main()
