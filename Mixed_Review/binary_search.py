"""Write a function, binary_search, that takes in a sorted list of numbers and a target. The function should return the index where the target can be found within the list. If the target is not found in the list, then return -1.

You may assume that the input array contains unique numbers sorted in increasing order.

Your function must implement the binary search algorithm."""

def binary_search(numbers, target):
  low = 0
  high = len(numbers) - 1
  mid = (low + high)//2
  while low <= high:
    if numbers[mid] == target:
      return mid
    if numbers[mid] < target:
      low = mid + 1
      mid = (low + high)//2
    else:
      high = mid - 1
      mid = (low + high)//2
      
  return -1


binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6


binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> -1


binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8) # -> 2


binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 28) # -> 8


binary_search([7, 9], 7) # -> 0


binary_search([7, 9], 9) # -> 1


binary_search([7, 9], 12) # -> -1


binary_search([7], 7) # -> 0


binary_search([], 7) # -> -1
