"""Write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters."""

from collections import deque

def decompress_braces1(string):
  stack = []
  queue = deque([])
  for char in string:
    if char != "}":
      stack.append(char)
    else:
      decompress(stack, queue)
  return "".join(stack)


def decompress1(stack, queue):
  while True:
    element = stack.pop()
    if element.isnumeric():
      segment = "".join(queue)
      segment = segment * int(element)
      stack.append(segment)
      queue.clear()
      break
    if element != "{":
      queue.appendleft(element)




def decompress_braces(string):
  stack = []
  for char in string:
    if char != "}":
      stack.append(char)
    else:
      decompress(stack)
  return "".join(stack)


def decompress(stack):
  segment = ""
  while True:
    element = stack.pop()
    if element.isnumeric():
      segment = segment * int(element)
      stack.append(segment)
      break
    if element != "{":
      segment = element + segment


decompress_braces("2{q}3{tu}v")
# -> qqtututuv 


decompress_braces("ch3{ao}")
# -> chaoaoao


decompress_braces("2{y3{o}}s")
# -> yoooyooos


decompress_braces("z3{a2{xy}b}")
# -> zaxyxybaxyxybaxyxyb 


decompress_braces("2{3{r4{e}r}io}")
# -> reeeerreeeerreeeerioreeeerreeeerreeeerio 


decompress_braces("go3{spinn2{ing}s}")
# -> gospinningingsspinningingsspinningings 


decompress_braces("2{l2{if}azu}l")
# -> lififazulififazul 


decompress_braces("3{al4{ec}2{icia}}")
# -> alececececiciaiciaalececececiciaiciaalececececiciaicia 
