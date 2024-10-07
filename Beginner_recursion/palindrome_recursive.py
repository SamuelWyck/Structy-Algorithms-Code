"""Write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.

You must solve this recursively."""

def palindrome(s):
  if len(s) <= 1:
    return True
  if s[0] == s[-1]:
    return palindrome(s[1:-1])
  else:
    return False

palindrome("pop") # -> True

palindrome("kayak") # -> True

palindrome("pops") # -> False

palindrome("boot") # -> False

palindrome("rotator") # -> True

palindrome("abcbca") # -> False

palindrome("") # -> True
