# O(nlogn) time / O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	firstRowShirt = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
	
	for idx in range(len(redShirtHeights)):		
		if firstRowShirt == 'RED':
			if redShirtHeights[idx] >= blueShirtHeights[idx]:
				return False
		else:
			if redShirtHeights[idx] <= blueShirtHeights[idx]:
				return False
			
	return True		


################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtHeights = [5, 8, 1, 3, 4]
        blueShirtHeights = [6, 9, 2, 4, 5]
        expected = True
        actual = program.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(actual, expected)
