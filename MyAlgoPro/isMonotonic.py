# O(n) time / O(1) space
def isMonotonic1(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
	    if direction == 0:
		    direction = array[i] - array[i - 1]
		    continue
	    if breakDirection(direction, array[i - 1], array[i]):
		    return False
		
    return True

def breakDirection(direction, previousInt, currentInt):
	difference = currentInt - previousInt
	if direction > 0:
		return difference < 0
	return difference > 0


# O(n) time / O(1) space
def isMonotonic2(array):
    if len(array) <= 2:
        return True
	
    isDecreasing = True
    isIncreasing = True
	
    for i in range(1, len(array)):
	    if array[i] < array[i - 1]: 
		    isIncreasing = False
	    if array[i] > array[i - 1]:
		    isDecreasing = False
			
    return isDecreasing or isIncreasing		    

#########################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = program.isMonotonic(array)
        self.assertEqual(actual, expected)