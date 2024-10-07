"""Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively."""

def fib(n, numbers={}):
  if n in numbers:
    return numbers[n]
  if n == 0:
    return 0
  if n == 1:
    return 1
    
  numbers[n] = (fib(n - 1, numbers) + fib(n - 2, numbers))
  return numbers[n]


def fib1(n, numbers=[0, 1], length=2):
  if n == 0:
    return 0
  if n == 1:
    return 1  
    
  if length - 1 != n:
    numbers.append((numbers[-1] + numbers[-2]))
    length += 1
  else:
    return numbers[n]
  return fib(n, numbers, length)


fib(0); # -> 0


fib(1); # -> 1


fib(2); # -> 1


fib(3); # -> 2


fib(4); # -> 3


fib(5); # -> 5


fib(35); # -> 9227465


fib(46); # -> 1836311903
