"""
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""
def longest_palindrome_subsequence(s: str) -> int:
    n = len(s)
    memo = {}

    def lps(lo, hi):
        if (lo, hi) in memo:
            return memo[(lo, hi)]
        if lo > hi:
            return 0
        if lo == hi:
            return 1
        if s[lo] == s[hi]:
            memo[(lo, hi)] = 2 + lps(lo + 1, hi - 1)
        else:
            memo[(lo, hi)] = max(lps(lo + 1, hi), lps(lo, hi - 1))
        return memo[(lo, hi)]
    
    return lps(0, n - 1)


if __name__ == "__main__":
    s = 'bbbab'
    print(longest_palindrome_subsequence(s))