"""Write a function, token_transform, that takes in a dictionary of tokens and a string. In the dictionary, the replacement values for a token may reference other tokens. The function should return a new string where tokens are replaced with their fully evaluated string values.

Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted and "$" is not used in the string except to enclose a token.

You may assume that there are no circular token dependencies."""

def token_transform(s, tokens):
  i = 0
  j = 1
  result = []
  while i < len(s):
    if s[i] != "$":
      result.append(s[i])
      i += 1
      j = i + 1
    elif s[j] != "$":
      j += 1
    else:
      key = s[i:j + 1]
      word = tokens[key]
      evaled_word = token_transform(word, tokens)
      tokens[key] = evaled_word
      result.append(evaled_word)
      i = j + 1
      j = i + 1
  return "".join(result)


tokens = {
  '$LOCATION$': '$ANIMAL$ park',
  '$ANIMAL$': 'dog',
}
token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the dog park!'


tokens = {
  '$ADJECTIVE_1$': "quick",
  '$ADJECTIVE_2$': "eager",
  '$ADVERBS$': "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
  '$VERB$': "hopped $DIRECTION$",
  '$DIRECTION$': "North",
}
token_transform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens)
# -> 'the quick fox quickly and eagerly hopped Northward'


tokens = {
  '$B$': "epicly $C$",
  '$A$': "pretty $B$ problem $D$",
  '$D$': "we have",
  '$C$': "clever",
}
token_transform("What a $A$ here!", tokens)
# -> 'What a pretty epicly clever problem we have here!'


tokens = {
  '$1$': "a$2$",
  '$2$': "b$3$",
  '$3$': "c$4$",
  '$4$': "d$5$",
  '$5$': "e$6$",
  '$6$': "f!",
}
token_transform("$1$ $1$ $1$ $1$ $1$ $1$ $4$ $4$", tokens)
# -> 'abcdef! abcdef! abcdef! abcdef! abcdef! abcdef! def! def!'


tokens = {
  '$0$': "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
  '$1$': "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
  '$2$': "$3$$3$$3$$3$$3$$3$$3$",
  '$3$': "$4$$4$$4$$4$$4$$4$",
  '$4$': "$5$$5$$5$$5$$5$",
  '$5$': "$6$$6$$6$$6$",
  '$6$': "$7$$7$$7$",
  '$7$': "$8$$8$",
  '$8$': "",
}
token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens)
# -> 'zzzzzzz'
