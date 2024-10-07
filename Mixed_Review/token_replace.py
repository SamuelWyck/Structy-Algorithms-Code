"""Write a function, token_replace, that takes in a dictionary of tokens and a string. The function should return a new string where tokens are replaced.

Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted and '$' is not used in the string except to enclose a token. Tokens should be replaced from left to right in the string."""

def token_replace1(s, tokens):
  stack = []
  sign_count = 0
  for char in s:
    if char == "$":
      sign_count += 1
      if sign_count == 2:
        replace(s, tokens, stack)
        sign_count = 0
      else:
        stack.append(char)
    else:
      stack.append(char)
  return "".join(stack)


def replace(string, tokens, stack):
  word = "$"
  while True:
    letter = stack.pop()
    word = letter + word
    if letter == "$":
      break
  word = tokens[word]
  stack.append(word)



def token_replace(s, tokens):
  i = 0
  j = 1
  result = ""
  while i < len(s):
    if s[i] != "$":
      result += s[i]
      i += 1
      j = i + 1
    elif s[j] != "$":
      j += 1
    else:
      word = s[i:j + 1]
      word = tokens[word]
      result += word
      i = j + 1
      j = i + 1
  return result


tokens = {
  '$LOCATION$': 'park',
  '$ANIMAL$': 'dog',
}
token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the park!'


tokens = {
  '$ADJECTIVE$': 'quick',
  '$VERB$': 'hopped',
  '$DIRECTION$': 'North'
}
token_replace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens)
# -> 'the quick fox hopped quickly Northward'


tokens = {
  '$greeting$': 'hey programmer',
}
token_replace('his greeting is always $greeting$.', tokens)
# -> 'his greeting is always hey programmer.'


tokens = {
  '$A$': 'lions',
  '$B$': 'tigers',
  '$C$': 'bears',
}
token_replace('$A$$B$$C$, oh my.', tokens)
# -> 'lionstigersbears, oh my.'


tokens = {
  '$A$': 'lions',
  '$B$': 'tigers',
  '$C$': 'bears',
}
token_replace('$B$', tokens)
# -> 'tigers'


tokens = {
  '$second$': 'beta',
  '$first$': 'alpha',
  '$third$': 'gamma',
}
token_replace('$first$second$third$', tokens)
# -> 'alphasecondgamma'
