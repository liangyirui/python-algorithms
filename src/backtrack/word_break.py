"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

def word_break(s: str, word_dict: list[str]) -> list[str]:
    word_set = set(word_dict)
    ans = []
    backtrack(s, word_set, [], ans, 0)
    return ans


def backtrack(s: str, word_set: set[str], path: list[str], paths: list[str], start: int) -> None:
    if start == len(s):
        paths.append(' '.join(path))
        return
    for end in range(start + 1, len(s) + 1):
        word = s[start:end]
        if word in word_set:
            path.append(word)
            backtrack(s, word_set, path, paths, end)
            path.pop()


def main():
    s = "catsanddog"
    word_dict = ['cat', 'cats', 'and', 'sand', 'dog']
    word_list = word_break(s, word_dict)
    print(word_list)


if __name__ == "__main__":
    main()