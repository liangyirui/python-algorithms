"""
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.
Return true if it is possible. Otherwise, return false.
"""
import collections

def is_possible_divide(nums: list[int], k: int) -> bool:
    n = len(nums)
    if n % k != 0:
        return False
    if k == 1:
        return True
    num_count = collections.Counter(nums)
    nums.sort()
    i = 0
    while i < n:
        start = nums[i]
        for j in range(k):
            if num_count[start + j] == 0:
                return False
            num_count[start + j] -= 1
        while i < n and num_count[nums[i]] == 0:
            i += 1
    return True


def main():
    nums = [3,2,1,2,3,4,3,4,5,9,10,11]
    k = 3
    print('Array can be divided in subarrays of', k, is_possible_divide(nums, k))


if __name__ == '__main__':
    main()
