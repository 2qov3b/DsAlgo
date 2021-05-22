def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

# O(log(n)) time / O(log(n)) space  
def binarySearchHelper1(array, target, left, right):
	if left > right:
		return -1
		
	middle = (left + right) // 2
	tempvalue = array[middle]

	if target == tempvalue:
		return middle
	elif target < tempvalue:
		return binarySearchHelper(array, target, left, middle - 1)
	else:
		return binarySearchHelper(array, target, middle + 1, right)
    
    
# O(log(n)) time / O(1) space    
def binarySearchHelper2(array, target, left, right):
    while left <= right:
	    middle = (left + right) // 2
	    tempvalue = array[middle]
	    
	    if target == tempvalue:
	    	return middle
	    elif target < tempvalue:
	    	right = middle -1
	    else:
	        left = middle + 1
		return -1        
	
  
##############################################################################
import program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
