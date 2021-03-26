# O(nlogn) time / O(n) space
def sortedSquaredArray1(array):
    sortedSquares = [0 for _ in array]
	
	for idx in range(len(array)):
		value = array[idx]
		sortedSquares[idx] = value * value
		
	sortedSquares.sort()
	return 	sortedSquares			 

# O(n) time / O(n) space
def sortedSquaredArray2(array):
  sortedSquares = [0 for _ in array]
	smallerIdx = 0
	largerIdx = len(array) - 1
	
	for idx in reversed(range(len(array))):
		smallValue = array[smallerIdx]
		largeValue = array[largerIdx]
		
    if abs(array[smallerIdx]) < abs(array[largerIdx]):
			sortedSquares[idx] = largeValue * largeValue
			largerIdx -= 1
		else:
			sortedSquares[idx] = smallValue * smallValue
			smallerIdx += 1
			
	return 	sortedSquares			 

######################################################################  
import program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = program.sortedSquaredArray(input)
        self.assertEqual(actual, expected)
