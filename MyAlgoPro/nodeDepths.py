# O(n) time / O(h) space - where n is the # of nodes; h is the height of tree.
def nodeDepths1(root):
	sumOfDepths = 0 
	stack = [{"node": root, "depth": 0}]
	
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths += depth
		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})
	return sumOfDepths	


# O(n) time / O(h) space - where n is the # of nodes; h is the height of tree.
def nodeDepths2(root, depth = 0):
	if root is None:
		return 0
  return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
    


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        
###################################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(2)
        root.left.left = program.BinaryTree(4)
        root.left.left.left = program.BinaryTree(8)
        root.left.left.right = program.BinaryTree(9)
        root.left.right = program.BinaryTree(5)
        root.right = program.BinaryTree(3)
        root.right.left = program.BinaryTree(6)
        root.right.right = program.BinaryTree(7)
        actual = program.nodeDepths(root)
        self.assertEqual(actual, 16)
