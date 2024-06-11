def heap_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def heapify(arr: list[int], n: int, i: int) -> None:
    root, left, right = i, 2 * i + 1, 2 * i + 2
    if left < n and arr[left] > arr[root]:
        root = left
    if right < n and arr[right] > arr[root]:
        root = right
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr, n, root)