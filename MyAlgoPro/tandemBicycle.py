# O(nlogn) time / 0(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	if fastest:
		redShirtSpeeds.sort(reverse=True)
	  blueShirtSpeeds.sort()
		maxSpeed = 0
		for idx in range(len(redShirtSpeeds)):
			maxSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
		return maxSpeed
	else:
		redShirtSpeeds.sort()
	  blueShirtSpeeds.sort()
		minSpeed = 0
		for idx in range(len(redShirtSpeeds)):
			minSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
		return minSpeed
  
################################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtSpeeds = [5, 5, 3, 9, 2]
        blueShirtSpeeds = [3, 6, 7, 2, 1]
        fastest = True
        expected = 32
        actual = program.tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
        self.assertEqual(actual, expected)
