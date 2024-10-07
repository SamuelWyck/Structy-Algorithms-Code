"""Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. The function should return the length of the longest subsequence of strictly increasing numbers.

A subsequence of a list can be created by deleting any items of the list, while maintaining the relative order of items."""

def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, float("-inf"), {}, 0)


def _max_increasing_subseq(numbers, prev, memo, i):
  if (prev, i) in memo:
    return memo[(prev, i)]
  if i == len(numbers):
    return 0

  if numbers[i] > prev:
    take = 1 + _max_increasing_subseq(numbers, numbers[i], memo, i + 1)
  else:
    take = float("-inf")
  dont_take = _max_increasing_subseq(numbers, prev, memo, i + 1)
  memo[(prev, i)] = max(take, dont_take)
  return memo[(prev, i)]
  

numbers = [4, 18, 20, 10, 12, 15, 19]
max_increasing_subseq(numbers) # -> 5


numbers = [12, 9, 2, 5, 4, 32, 90, 20]
max_increasing_subseq(numbers) # -> 4


numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
max_increasing_subseq(numbers) # -> 5


numbers = [7, 14, 10, 12]
max_increasing_subseq(numbers) # -> 3


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
max_increasing_subseq(numbers) # -> 21


numbers = [
  1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
  104,
]
max_increasing_subseq(numbers) # -> 23


numbers = [
  1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
  17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
]
max_increasing_subseq(numbers) # -> 27


numbers = [
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1
]
max_increasing_subseq(numbers) # -> 1
