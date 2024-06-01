"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
"""

def single_number(nums: list[int]) -> list[int]:
    xor = 0
    for num in nums:
        xor ^= num
    
    diff = xor & (-xor)
    a = b = 0
    for num in nums:
        if (num & diff) != 0:
            a ^= num
        else:
            b ^= num
    return [a, b]


def main():
    nums = [1, 2, 1, 3, 2, 5]
    output = single_number(nums)
    print(output)


if __name__ == "__main__":
    main()