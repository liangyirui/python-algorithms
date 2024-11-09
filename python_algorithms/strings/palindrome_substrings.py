def is_palindrome(s: str) -> bool:
    if not s:
        return False
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True


def dfs(s: str, path: list[str], paths: list[list[str]]) -> None:
    if not s:
        paths.append(path)
        return
    for i in range(1, len(s) + 1):
        if is_palindrome(s[:i]):
            dfs(s[i:], path + [s[:i]], paths)


def main():
    s = "aabcddb"
    paths = []
    dfs(s, [], paths)
    print(paths)


if __name__ == "__main__":
    main()
