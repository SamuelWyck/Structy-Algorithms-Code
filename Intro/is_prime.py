"""Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

You can assume that the input number is a positive integer."""

import math
def is_prime(n):
  if n == 1:
    return False
  for i in range(2, (int(math.sqrt(n) + 1))):
    if n % i == 0:
      return False
  return True

is_prime(2) # -> True
is_prime(3) # -> True
is_prime(4) # -> False
is_prime(5) # -> True
is_prime(6) # -> False
is_prime(7) # -> True
is_prime(8) # -> False
is_prime(25) # -> False
is_prime(31) # -> True
is_prime(2017) # -> True
is_prime(2048) # -> False
is_prime(1) # -> False
is_prime(713) # -> False
