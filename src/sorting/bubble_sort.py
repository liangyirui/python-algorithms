def bubble_sort(arr: list[int]):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    arr = [5,1,2,3,4]
    bubble_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()