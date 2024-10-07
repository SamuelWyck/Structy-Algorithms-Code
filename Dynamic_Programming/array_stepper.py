"""Write a function, array_stepper, that takes in a list of numbers as an argument. You start at the first position of the list. The function should return a boolean indicating whether or not it is possible to reach the last position of the list. When situated at some position of the list, you may take a maximum number of steps based on the number at that position.

For example, given:

    idx =  0  1  2  3  4  5
numbers = [2, 4, 2, 0, 0, 1]

The answer is True.
We start at idx 0, we could take 1 step or 2 steps forward.
The correct choice is to take 1 step to idx 1.
Then take 4 steps forward to the end at idx 5."""

def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})


def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]
  if i >= len(numbers):
    return False
  if i == len(numbers) - 1:
    return True
  if numbers[i] == 0:
    return False

  for num in range(1, numbers[i] + 1):
    if _array_stepper(numbers, i + num, memo):
      memo[i] = True
      return True
  memo[i] = False
  return False


array_stepper([2, 4, 2, 0, 0, 1]) # -> True


array_stepper([2, 3, 2, 0, 0, 1]) # -> False


array_stepper([3, 1, 3, 1, 0, 1]) # -> True


array_stepper([4, 1, 5, 1, 1, 1, 0, 4]) # -> True


array_stepper([4, 1, 2, 1, 1, 1, 0, 4]) # -> False


array_stepper([1, 1, 1, 1, 1, 0]) # -> True


array_stepper([1, 1, 1, 1, 0, 0]) # -> False


array_stepper([ 
  31, 30, 29, 28, 27,
  26, 25, 24, 23, 22,
  21, 20, 19, 18, 17,
  16, 15, 14, 13, 12,
  11, 10, 9, 8, 7, 6,
  5, 3, 2, 1, 0, 0, 0
]) # -> False

