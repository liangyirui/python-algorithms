def merge_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    aux = [0] * n
    sort(arr, aux, 0, n - 1)
    return arr

def sort(arr: list[int], aux: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2
    sort(arr, aux, lo, mid)
    sort(arr, aux, mid + 1, hi)
    merge(arr, aux, lo, mid, hi)


def merge(arr: list[int], aux: list[int], lo: int, mid: int, hi: int) -> None:
    for i in range(lo, hi + 1):
        aux[i] = arr[i]
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1



def main():
    nums = [5, 1, 1, 2, 0, 0]
    print(nums)
    print(merge_sort(nums))


if __name__ == '__main__':
    main()