"""Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>
for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern."""

def uncompress2(s): #my first solution
  nums = []
  chars = []
  num_index = -1
  last_index_num = False
  for char in s:
    if char.isnumeric():
      if last_index_num:
        nums[num_index] = nums[num_index] + char
      else:
        nums.append(char)
        num_index += 1
        last_index_num = True
    else:
      last_index_num = False
      chars.append(char)
  string = ""
  for num, char in zip(nums, chars):
    for _ in range(int(num)):
      string += char
  return string

def uncompress(s):
  i = 0
  j = 0
  string = ""
  for char in s:
    if char.isnumeric():
      j += 1
    else:
      number = s[i:j]
      string += (char * int(number))
      j += 1
      i = j
  return string

uncompress("2c3a1t") # -> 'ccaaat'
uncompress("4s2b") # -> 'ssssbb'
uncompress("2p1o5p") # -> 'ppoppppp'
uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
