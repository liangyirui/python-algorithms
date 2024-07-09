"""
Given a string s and an integer k, return true if s is a k-palindrome.
A string s k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.
"""

def is_valid_palindrome(s: str, k: int) -> bool:
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
	s = "abcdeca"
	k = 2
	print(is_valid_palindrome(s, k))
