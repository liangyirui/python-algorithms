"""
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
You result should not contain any brackets.
"""

def reverse_parentheses(s: str) -> str:
	n = len(s)
	open_indices = []
	pair = [0] * n
	for i, ch in enumerate(s):
		if ch == '(':
			open_indices.append(i)
		if ch == ')':
			j = open_indices.pop()
			pair[i] = j
			pair[j] = i
	
	sb = []
	curr_index = 0
	direction = 1
	while curr_index < n:
		if s[curr_index] == '(' or s[curr_index] == ')':
			curr_index = pair[curr_index]
			direction = -direction
		else:
			sb.append(s[curr_index])
		curr_index += direction
	return ''.join(sb)
