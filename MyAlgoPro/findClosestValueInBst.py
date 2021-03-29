# Average: O(log(n)) time / O(log(n)) space
# Worst: O(n) time / O(n) space 
def findClosestValueInBst1(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closer):
	if tree is None:
		return closer
	if abs(target - closer) > abs(target - tree.value):
		closer = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closer)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closer)
	else:
		return closer
		

# Average: O(log(n)) time / O(1) space
# Worst: O(n) time / O(1) space 
def findClosestValueInBst2(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closer):
	currentNode = tree
	while currentNode is not None:
		if abs(target - closer) > abs(target - currentNode.value):
			closer = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closer        

# This is the class of the input tree.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
######################################################################  
import program
import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = program.findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)
