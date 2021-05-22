# Best: O(n) time / O(1) space
# Average: O(n^2) time / O(1) space
# Worst: O(n^2) time / O(1) space
def bubbleSort(array):
	isSorted = False
	counter = 0
	while isSorted is not True:
		isSorted = True
		for i in range(len(array) - 1 - counter):
			if array[i] > array[i + 1]:
				swap(i, i + 1, array)
				isSorted = False
		counter += 1		
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

  
#########################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.bubbleSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
