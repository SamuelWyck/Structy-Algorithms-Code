"""Write a function, fibonacci, that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

You must solve this recursively."""

def fibonacci1(n, numbers=None):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  if numbers is None:
    numbers = [0, 1]
  if len(numbers) - 1 != n:
    numbers.append((numbers[-1] + numbers[-2]))
  else:
    return numbers[n]
  return fibonacci(n, numbers)

def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(0); # -> 0

fibonacci(1); # -> 1

fibonacci(2); # -> 1

fibonacci(3); # -> 2

fibonacci(4); # -> 3

fibonacci(5); # -> 5

fibonacci(8); # -> 21
