"""Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order."""

def anagrams(s1, s2):
  s1 = sorted(s1)
  s2 = sorted(s2)
  if s1 == s2:
    return True
  return False


anagrams('restful', 'fluster') # -> True
anagrams('cats', 'tocs') # -> False
anagrams('monkeyswrite', 'newyorktimes') # -> True
anagrams('paper', 'reapa') # -> False
anagrams('elbow', 'below') # -> True
anagrams('tax', 'taxi') # -> False
anagrams('night', 'thing') # -> True
anagrams('abbc', 'aabc') # -> False
anagrams('po', 'popp') # -> false
anagrams('pp', 'oo') # -> false
