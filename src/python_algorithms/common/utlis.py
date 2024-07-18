from list_node import ListNode, linked_list_to_list, list_to_linked_list


def print_matrix(matrix: list[list[int]]) -> None:
    sb = []
    for i, row in enumerate(matrix):
        if i == 0:
            sb.append(str(row))
        else:
            sb.append(" " + str(row))
    print("[" + ",\n".join(sb) + "]")


def print_linked_list(head: ListNode | None) -> None:
    arr = linked_list_to_list(head)
    print(" -> ".join([str(item) for item in arr]))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    head = list_to_linked_list(arr)
    print_linked_list(head)
