# O(nlogn) time / O(1) space
def nonConstructibleChange(coins):
  coins.sort()
	
	createdChange = 0
	for coin in coins:
		if coin > createdChange + 1:
			#return createdChange + 1
			break
		createdChange += coin
		
	return createdChange + 1


##################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = program.nonConstructibleChange(input)
        self.assertEqual(actual, expected)
