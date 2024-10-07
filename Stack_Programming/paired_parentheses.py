"""Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'."""

def paired_parentheses(string):
  count = 0
  for char in string:
    if char == "(":
      count += 1
    elif char == ")":
      count -= 1
    if count < 0:
      return False
  if count > 0:
    return False
  return True


paired_parentheses("(david)((abby))") # -> True


paired_parentheses("()rose(jeff") # -> False


paired_parentheses(")(") # -> False


paired_parentheses("()") # -> True


paired_parentheses("(((potato())))") # -> True


paired_parentheses("(())(water)()") # -> True


paired_parentheses("(())(water()()") # -> False


paired_parentheses("") # -> True


paired_parentheses("))()") # False
