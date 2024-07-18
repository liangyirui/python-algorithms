"""
Given an m * n matrix mat, return an array of all elements of the array in diagonal order.
"""

from collections import defaultdict

def find_diagonal_order(mat: list[list[int]]) -> list[int]:
	m, n = len(mat), len(mat[0])
	index_value = defaultdict(list)
	for i, row in enumerate(mat):
		for j, val in enumerate(row):
			index_value[i + j].append(val)
	
	value_by_order = []
	for key, value_list in index_value.items():
		if key % 2 == 0:
			value_by_order.extend(value_list[::-1])
		else:
			value_by_order.extend(value_list)
	return value_by_order
