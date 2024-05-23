def backtrack(nums: list[int], start: int, path: list[int], paths: list[list[int]]) -> None:
    paths.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(nums, i + 1, path, paths)
        path.pop()


def main() -> None:
    nums = [1, 2, 3, 4]
    paths = []
    backtrack(nums, 0, [], paths)
    print(len(paths))
    print(paths)


if __name__ == "__main__":
    main()