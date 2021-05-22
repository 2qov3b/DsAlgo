# O(n^2) time / O(n) space
def threeNumberSum(array, targetSum):
	array.sort()
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		
		while left < right:
			threeSum = array[i] + array[left] + array[right]
			if threeSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
			elif threeSum < targetSum:
			    left += 1
			elif threeSum > targetSum:
			    right -= 1
				
	return triplets	

#######################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
