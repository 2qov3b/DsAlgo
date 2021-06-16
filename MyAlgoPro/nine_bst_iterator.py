# O(n) time / O(n) space
def inorder_traversal(root):
    if root is None:
        return []

    # Create a dummy node and the right pointer to root
    # Put the dummy node to a stack,
    # and the current position of the iterator is the top of stack - dummy
    dummy = TreeNode(0)
    dummy.right = root
    stack = [dummy]

    inorder = []
    # When move iterator to next node, the top of stack will point to next node
    while stack:
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if stack:
            inorder.append(stack[-1])
    return inorder                    