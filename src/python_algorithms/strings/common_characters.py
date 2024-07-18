"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
"""

import collections


def common_characters(words: list[str]) -> list[str]:
    n = len(words)
    common_chars = []
    freq = collections.Counter(words[0])
    for i in range(1, n):
        curr_freq = collections.Counter(words[i])
        for ch, count in freq.items():
            freq[ch] = min(freq[ch], curr_freq[ch])

    for ch, count in freq.items():
        for _ in range(count):
            common_chars.append(ch)
    return common_chars


def main():
    words = ["bella", "label", "roller"]
    common_chars = common_characters(words)
    print(common_chars)


if __name__ == "__main__":
    main()
