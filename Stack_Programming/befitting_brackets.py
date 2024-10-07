"""Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }"""

def befitting_brackets(string):
  stack = []
  for char in string:
    if char == "(" or char == "{" or char == "[":
      stack.append(char)
    else:
      if not stack:
        return False
      prev = stack.pop()
      if prev == "(" and char != ")":
        return False
      elif prev == "{" and char != "}":
        return False
      elif prev == "[" and char != "]":
        return False
  if not stack:
    return True
  return False


befitting_brackets('(){}[](())') # -> True


befitting_brackets('({[]})') # -> True


befitting_brackets('[][}') # -> False


befitting_brackets('{[]}({}') # -> False


befitting_brackets('[]{}(}[]') # -> False


befitting_brackets('[]{}()[]') # -> True


befitting_brackets(']{}') # -> False


befitting_brackets('') # -> True


befitting_brackets("{[(}])") # -> False

