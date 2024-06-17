"""
We are given n different types of stickers. Each sticker has a lowercase English word on it.
You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
Return the miniumu number of stickers that you need to spell out target. If the task is impossible, return -1.
Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.
"""

def min_stickers(stickers: list[str], target: str) -> int:
    n = len(stickers)
    stickers_map = [[0] * 26 for _ in range(n)]
    for i, sticker in enumerate(stickers):
        for ch in sticker:
            num = ord(ch) - ord('a')
            stickers_map[i][num] += 1
    
    memo = {}
    memo[''] = 0
    return dfs(memo, stickers_map, target)


def dfs(memo: dict[str], str_map: list[list[int]], target: str) -> int:
    if target in memo:
        return memo[target]
    n = len(str_map)
    sb = [0] * 26
    for ch in target:
        sb[ord(ch) - ord('a')] += 1

    result = float('inf')
    for i in range(n):
        # optimization: ignore a sticker if it doesn't contain target[0]
        if str_map[i][ord(target[0]) - ord('a')] == 0:
            continue
        new_target = ''
        for j in range(26):
            if sb[j] > str_map[i][j]:
                new_target += chr(ord('a') + j) * (sb[j] - str_map[i][j])
        dp = dfs(memo, str_map, new_target)
        if dp != -1:
            result = min(result, dp + 1)
    memo[target] = -1 if result == float('inf') else result
    return memo[target]



if __name__ == "__main__":
    stickers = ['with', 'example', 'science']
    target = 'thehat'
    print(min_stickers(stickers, target))