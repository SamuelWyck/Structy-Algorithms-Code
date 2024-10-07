"""Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The function should return True if the first word should appear before the second word if lexically-ordered according to the given alphabet order. If the second word should appear first, then return False.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters."""

def lexical_order1(word_1, word_2, alphabet):
  if word_1 == "":
    return True
  if word_2 == "":
    return False
  rank1 = alphabet.find(word_1[0])
  rank2 = alphabet.find(word_2[0])
  if rank1 < rank2:
    return True
  if rank1 > rank2:
    return False

  return lexical_order(word_1[1:], word_2[1:], alphabet)



def lexical_order2(word_1, word_2, alphabet):
  return _lexical_order(word_1, word_2, 0, 0, alphabet)


def _lexical_order(word_1, word_2, s1, s2, alphabet):
  if s1 == len(word_1):
    return True
  if s2 == len(word_2):
    return False
  rank1 = alphabet.find(word_1[s1])
  rank2 = alphabet.find(word_2[s2])
  if rank1 < rank2:
    return True
  if rank1 > rank2:
    return False

  return _lexical_order(word_1, word_2, s1 + 1, s2 + 1, alphabet)



def lexical_order3(word_1, word_2, alphabet):
  i = 0
  while i < len(word_1) and i < len(word_2):
    if word_1[i] != word_2[i]:
      rank1 = alphabet.find(word_1[i])
      rank2 = alphabet.find(word_2[i])
      if rank1 > rank2:
        return False
      else:
        return True
    i += 1

  if i == len(word_2) and i != len(word_1):
    return False
  return True



def lexical_order(word_1, word_2, alphabet):
  max_len = max(len(word_1), len(word_2))
  for i in range(max_len):
    if i < len(word_1):
      rank1 = alphabet.find(word_1[i])
    else:
      rank1 = -1
    if i < len(word_2):
      rank2 = alphabet.find(word_2[i])
    else:
      rank2 = -1
    if rank1 > rank2:
      return False
    elif rank1 < rank2:
      return True
  return True


alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("apple", "dock", alphabet) # -> True


alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("apple", "ample", alphabet) # -> False


alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("app", "application", alphabet) # -> True


alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("backs", "backdoor", alphabet) # -> False


alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("zoo", "dinner", alphabet) # -> True


alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("leaper", "leap", alphabet) # -> False


alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("backs", "backdoor", alphabet) # -> True


alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("semper", "semper", alphabet) # -> True
