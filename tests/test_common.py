from python_algorithms.common.list_node import list_to_linked_list
from python_algorithms.common.utils import print_linked_list, print_matrix

arr = [1, 2, 3, 4, 5, 6]
mat = [[1, 2, 4], [1, 2, 4], [2, 5, 4]]
head = list_to_linked_list(arr)
print_linked_list(head)

print_matrix(mat)
