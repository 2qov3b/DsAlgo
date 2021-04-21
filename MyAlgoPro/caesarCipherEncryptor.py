# O(n) time / O(n) space
def caesarCipherEncryptor(string, key):
  newLetters = []
	newKey = key % 26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

#################################################
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.caesarCipherEncryptor("xyz", 2), "zab")
