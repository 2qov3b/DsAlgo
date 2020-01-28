# Time Complexity: O(NMlogM). N:# of strings, M:Length of the largest string.
# A function finds the string having the minimum length and returns the length.
def findMinLength(strList):
  return len(min(arr, key = len))

def allContainsPrefix(strList, str, start, end):
  for i in range(0, len(strList)):
    word = strList[i]
    for j in range(start, end + 1):
      if word[j] != str[j]:
        return False
  return True

# A function returns the longest common prefix from the array of strings
def CommonPrefix(strList):
  index = findMinLength(strList)
  prefix = "" # result
 
  # In-place binary search on the first string of the arr in the range 0 to index
  low, high = 0, index - 1
  while low <= high:
    # Avoids (low + high)/2 overflow
    mid = int(low + (high - low) / 2)
    if allContainsPrefix(strList, strList[0], low, mid):
      # Append substring to result if all strings in the arr contains the prefix
      prefix = prefix + strList[0][low:mid + 1]

      # And then go for the right part
      low = mid + 1
    else:
      # Go for the left part
      high = mid - 1
  return prefix

# Test code
arr = ["bub", "bubby", "bubble", "bububu", "buberly"] 
lcp = CommonPrefix(arr)

if len(lcp) > 0:
  print("The longest common prefix is " + str(lcp))
else:
  print("There is no common prefix")
  
