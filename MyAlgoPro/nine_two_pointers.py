#########################################################
## Same direction two pointers - patition in quicksort ##
def patition(self, A, start, end):
    if start >= end:
        return

    left, right = start, end
    # key point 1: pivot is the value, not the index
    pivot = A[(start + end) // 2]

    # key point 2: every time you compare left & right, it should be
    # left <= right not left < right
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1


#####################################
## Opposite direction two pointers ##
left = position
right = position + 1
while left >= 0 and right < len(s):
    if left and right: # Condition which stop left & right
        break
    left -= 1
    right += 1


#################################
## Same direction two pointers ##
j = 0
for i in range(n):
    # keep looping until satify condition
    while j < n and X is true: # X: Don't satify condition beteen i & j
        j += 1
    if Y is true: # Y: Satify condition beteen i & j
        pass # Logic to deal with i to j


########################
## Merge two pointers ##
def merge(list1, list2):
    new_list = []
    i, j = 0, 0

    # Only merge by moving i, j
    # No use list1.pop(0) -> pop(0): O(n) time
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    # Move rest to new_list
    # No use new_list.extend(list1[i:]) -> list1[i:] will cost extra space
    while i < len(list1):
        new_list.append(list1[i])
        i += 1
    while j < len(list2):
        new_list.append(list2[j])
        j += 1

    return new_list