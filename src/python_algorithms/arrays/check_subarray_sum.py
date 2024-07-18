"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
1. Its length is at least two, and
2. THe sum of the elenents of the subarray is a multiple of k.
"""


def check_subarray_sum(nums: list[int], k: int) -> bool:
    # if a - b is a multiple of k, a % k == b % k
    # use prefix sum and hash table
    n = len(nums)
    if n <= 1:
        return False
    if k == 1:
        return True
    prefix_mod = 0
    mod_seen = {0: -1}
    for i, num in enumerate(nums):
        prefix_mod = (prefix_mod + num) % k
        if prefix_mod in mod_seen:
            if i - mod_seen[prefix_mod] > 1:
                return True
        else:
            mod_seen[prefix_mod] = i
    return False


def main():
    nums = [23, 2, 6, 4, 7]
    k = 6
    print(nums, k, check_subarray_sum(nums, k))


if __name__ == "__main__":
    main()
