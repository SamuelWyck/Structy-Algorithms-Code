"""Write a function, reverse_string, that takes in a string as an argument. The function should return the string with its characters in reverse order. You must do this recursively."""

def reverse_string(s):
  if s == "":
    return ""
  return reverse_string(s[1:]) + s[0]

reverse_string("hello") # -> "olleh"

reverse_string("abcdefg") # -> "gfedcba"

reverse_string("stopwatch") # -> "hctawpots"

reverse_string("") # -> ""
