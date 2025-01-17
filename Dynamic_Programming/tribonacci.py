"""Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively."""

def tribonacci(n):
  return _tribonacci(n, {})


def _tribonacci(n, numbers):
  if n in numbers:
    return numbers[n]
  if n <= 1:
    return 0
  if n == 2:
    return 1

  numbers[n] = (_tribonacci(n - 3, numbers) + _tribonacci(n - 2, numbers) +  
  _tribonacci(n - 1, numbers))
  return numbers[n]


tribonacci(0) # -> 0


tribonacci(0) # -> 0


tribonacci(2) # -> 1


tribonacci(5) # -> 4


tribonacci(7) # -> 13


tribonacci(14) # -> 927


tribonacci(20) # -> 35890


tribonacci(37) # -> 1132436852
