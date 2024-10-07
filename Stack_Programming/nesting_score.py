"""Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:

[] is worth 1 point
XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
[S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring

You may assume that the input only contains well-formed square brackets."""

def nesting_score1(string):
  stack = []
  for char in string:
    if char == "]":
      evaluate(stack)   
    else:
      stack.append(char)
  return sum(stack)


def evaluate(stack):
  inner_score = 0
  while True:
    element = stack.pop()
    if element == "[":
      if inner_score > 0:
        stack.append(2 * inner_score)
      else:
        stack.append(1)
      break
    else:
      inner_score += element   



def nesting_score(string):
  stack = [0]
  for char in string:
    if char == "]":
      value = stack.pop()
      if value == 0:
        stack[-1] += 1
      else:
        value = value * 2
        stack[-1] += value
    else:
      stack.append(0)
  return stack[0]


nesting_score("[]") # -> 1


nesting_score("[][][]") # -> 3


nesting_score("[[]]") # -> 2


nesting_score("[[][]]") # -> 4


nesting_score("[[][][]]") # -> 6


nesting_score("[[][]][]") # -> 5


nesting_score("[][[][]][[]]") # -> 7


nesting_score("[[[[[[[][]]]]]]][]") # -> 129


nesting_score("") # -> 0
