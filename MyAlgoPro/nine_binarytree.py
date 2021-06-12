# O(n) time / O(n) space
def divide_conquer(root):
    # Deal with node == null
    # Don't care node == leaf
    if root is None:
        return

    # Deal with left/right subtree
    left_result = divide_conquer(node.left)
    right_result = divide_conquer(node.right)

    # Merge the result
    result = merge(left_result, right_result)

    return result 