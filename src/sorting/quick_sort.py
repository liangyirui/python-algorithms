import random


def quick_sort(arr: list[int]) -> None:
    random.shuffle(arr)
    sort(arr, 0, len(arr) - 1)


def sort(arr: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    mid = partition(arr, lo, hi)
    sort(arr, lo, mid - 1)
    sort(arr, mid + 1, hi)


def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = lo
    while True:
        if arr[lo] < arr[pivot]:
            lo += 1
        elif arr[hi] > arr[pivot]:
            hi -= 1
        elif lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1
        else:
            arr[pivot], arr[hi] = arr[hi], arr[pivot]
            break
    return hi


def main():
    arr = [1, 3, 5, 6, 3]
    quick_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
