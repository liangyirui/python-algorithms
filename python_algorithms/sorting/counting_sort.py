def counting_sort(arr: list[int]) -> list[int]:
    max_val = max(arr)
    n = len(arr)
    count_arr = [0] * (max_val + 1)
    for num in arr:
        count_arr[num] += 1
    for i in range(1, max_val + 1):
        count_arr[i] += count_arr[i - 1]

    sorted_arr = [0] * n
    for i in range(n - 1, -1, -1):
        sorted_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    return sorted_arr


if __name__ == "__main__":
    arr = [4, 3, 12, 1, 1, 5, 0, 3, 9]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)
