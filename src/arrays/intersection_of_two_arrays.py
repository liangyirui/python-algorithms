"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    freq = {}
    for num in nums1:
        freq[num] = freq.get(num, 0) + 1
    ans = []
    for num in nums2:
        if num in freq and freq[num] > 0:
            ans.append(num)
            freq[num] -= 1
    return ans


if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersect(nums1, nums2))
