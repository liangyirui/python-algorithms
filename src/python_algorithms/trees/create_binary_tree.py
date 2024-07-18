"""
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.
The test cases will be generated such that the binary tree is valid.
"""

from binary_tree import TreeNode


def create_binary_tree(descriptions: list[list[int]]) -> TreeNode | None:
    node_map = {}
    children = set()
    for parent_val, child_val, is_left in descriptions:
        if parent_val not in node_map:
            node_map[parent_val] = TreeNode(parent_val)
        if child_val not in node_map:
            node_map[child_val] = TreeNode(child_val)
        if is_left == 1:
            node_map[parent_val].left = node_map[child_val]
        else:
            node_map[parent_val].right = node_map[child_val]
        children.add(child_val)

    for node in node_map.values():
        if node.val not in children:
            return node
    return None


if __name__ == "__main__":
    descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    print(f"The root node is {create_binary_tree(descriptions)}")
