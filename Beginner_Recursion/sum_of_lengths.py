"""Write a function sumOfLengths that takes in a list of strings and returns the total length of the strings.

You must solve this recursively."""

def sum_of_lengths(strings):
  if not strings:
    return 0
  return len(strings.pop()) + sum_of_lengths(strings)

sum_of_lengths(['goat', 'cat', 'purple']) # -> 13

sum_of_lengths(['bike', 'at', 'pencils', 'phone']) # -> 18

sum_of_lengths([]) # -> 0

sum_of_lengths(['', ' ', '  ', '   ', '    ', '     ']) # -> 15

sum_of_lengths(['0', '313', '1234567890']) # -> 14 
