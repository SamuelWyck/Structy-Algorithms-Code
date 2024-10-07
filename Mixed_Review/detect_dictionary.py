"""Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string. The function should return a boolean indicating whether or not all words of the dictionary are lexically-ordered according to the alphabet.

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters."""

def detect_dictionary(dictionary, alphabet):
  for i in range(len(dictionary) - 1):
    if not lexi_ordered(dictionary[i], dictionary[i + 1], alphabet):
      return False
  return True
      

def lexi_ordered(word_1, word_2, alphabet):
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
    if rank1 < rank2:
      return True
    elif rank1 > rank2:
      return False
  return True


dictionary = ["zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> True


dictionary = ["zoo", "tack", "tick", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> False


dictionary = ["zoos", "zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> False


dictionary = ["miles", "milestone", "proper", "process", "goal"]
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> True


dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> True


dictionary = ["miles", "milestone", "pint", "proper", "process","goal", "apple"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> False
