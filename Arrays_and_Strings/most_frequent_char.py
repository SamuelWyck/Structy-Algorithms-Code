"""Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty."""

def most_frequent_char(s):
  char_count = {}
  for char in s:
    if char not in char_count:
      char_count[char] = 1
    elif char in char_count:
      char_count[char] += 1
  answer = ["a", 0]
  for key in char_count:
    if char_count[key] > answer[1]:
      answer[0] = key
      answer[1] = char_count[key]
  return answer[0]

most_frequent_char('bookeeper') # -> 'e'
most_frequent_char('david') # -> 'd'
most_frequent_char('abby') # -> 'b'
most_frequent_char('mississippi') # -> 'i'
most_frequent_char('potato') # -> 'o'
most_frequent_char('eleventennine') # -> 'e'
most_frequent_char('riverbed') # -> 'r'
