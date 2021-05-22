# O(n) time / O(d) space - where n is the # of idx in the array, d is the greatest depth of array
def productSum(array, multiplier = 1):
	sum = 0
	for idx in array:
		if type(idx) == list:
			sum += productSum(idx, multiplier + 1)
		else:
			sum += idx
	return sum * multiplier		

##################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(program.productSum(test), 12)
