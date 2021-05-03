# O(n) time / O(1) space
def findThreeLargestNumbers(array):
  topThreeArray = [None, None, None]
	for num in array:
		sortHelper(topThreeArray, num)
	return topThreeArray	
	
def sortHelper(topThreeArray, num):
	if topThreeArray[2] is None or num > topThreeArray[2]:
	    updateHelper(topThreeArray, num, 2)
	elif topThreeArray[1] is None or num > topThreeArray[1]:
		updateHelper(topThreeArray, num, 1)
	elif topThreeArray[0] is None or num > topThreeArray[0]:	
        updateHelper(topThreeArray, num, 0)
		
def updateHelper(array, num, idx):
	for i in range(idx + 1):
		if i == idx:
		    array[i] = num
		else:
			array[i] = array[i + 1]
      
#################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])
