# O(nlog(n) + mlog(m)) time / O(1) space
def smallestDifference(arrayOne, arrayTwo):
  arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	curDiff = float("inf")
	smallestDiff = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		leftNum = arrayOne[idxOne]
		rightNum = arrayTwo[idxTwo]
		if leftNum < rightNum:
			curDiff = rightNum - leftNum
			idxOne += 1
		elif leftNum > rightNum:
			curDiff = leftNum - rightNum
			idxTwo += 1
		else:
			return [leftNum, rightNum]
		if smallestDiff > curDiff:
			smallestDiff = curDiff
			smallestPair = [leftNum, rightNum]
	return smallestPair	

####################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])
