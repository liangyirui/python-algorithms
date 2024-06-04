"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""

def longest_palindrome(s: str) -> int:
    freq = [0] * 256
    for ch in s:
        freq[ord(ch)] += 1
    count = 0
    for num in freq:
        count += (num // 2) * 2
    if count < len(s):
        return count + 1
    return count


def main():
    s = 'abccccdd'
    print(longest_palindrome(s))


if __name__ == '__main__':
    main()