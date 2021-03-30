# O(n) time / O(n) space - where n is the # of nodes in the Binary Tree
def branchSums(root):
  sums = []
	branchSumsHelper(root, 0, sums)
	return sums

def branchSumsHelper(node, runningSum, sums):
	if node is None:
		return
	
	nextRunningSum = runningSum + node.value
	
	if node.left is None and node.right is None:
		sums.append(nextRunningSum)
		return
	
	branchSumsHelper(node.left, nextRunningSum, sums)
	branchSumsHelper(node.right, nextRunningSum, sums)
  
######################################################################  
import program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(program.branchSums(tree), [15, 16, 18, 10, 11])


class BinaryTree(program.BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
