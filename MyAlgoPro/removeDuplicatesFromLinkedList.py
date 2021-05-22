class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time / O(1) space - where n is the # of nodes in the LinkedList
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
	
    while currentNode is not None:
	    nextNode = currentNode.next
		
	    while nextNode is not None and nextNode.value == currentNode.value:
		    nextNode = nextNode.next

	    currentNode.next = nextNode
	    currentNode = nextNode
	
    return linkedList



##############################################################################
import program
import unittest


class LinkedList(program.LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        actual = program.removeDuplicatesFromLinkedList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())
