# O(nlogn) time / O(1) space - where n is the # of queries
def minimumWaitingTime(queries):
	# queries = [3, 2, 1, 2, 6] -> [1, 2, 2, 3, 6]
  queries.sort()
	sum = 0
	
	# 1x4 + 2x3 + 2x2 + 3x1 = 17
	for a in enumerate(queries):
		sum += a[1] * (len(queries) - a[0] - 1)
	return sum


######################################################################  
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        queries = [3, 2, 1, 2, 6]
        expected = 17
        actual = program.minimumWaitingTime(queries)
        self.assertEqual(actual, expected)
