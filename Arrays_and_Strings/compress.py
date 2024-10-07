"""Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'

You can assume that the input only contains alphabetic characters."""

def compress(s):
  i = 0 
  char_count = 0
  char = s[0]
  string = ""
  while i < len(s):
    if s[i] == char:
      char_count += 1
      i += 1
      if i == len(s):
        if char_count > 1:
          string += (str(char_count) + char)
        else:
          string += char
    else:
      if char_count > 1:
        string += (str(char_count) + char)
      else:
        string += char
      char_count = 1
      char = s[i]
      i += 1
      if i == len(s):
        if char_count > 1:
          string += (str(char_count) + char)
        else:
          string += char
      
  return string

compress('ccaaatsss') # -> '2c3at3s'
compress('ssssbbz') # -> '4s2bz'
compress('ppoppppp') # -> '2po5p'
compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); 
# -> '127y'
