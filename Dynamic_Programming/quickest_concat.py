"""Write a function, quickest_concat, that takes in a string and a list of words as arguments. The function should return the minimum number of words needed to build the string by concatenating words of the list. If it is not possible to build the string, then return -1.

You may use words of the list as many times as needed."""

def quickest_concat(s, words):
  result = _quickest_concat(s, words, {})
  if result == float("inf"):
    return -1
  return result


def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]
  if len(s) == 0:
    return 0

  concats = float("inf")
  for word in words:
    if s.startswith(word):
      concats = min(concats, 1 + _quickest_concat(s[len(word):], words, memo))

  memo[s] = concats
  return memo[s]


quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2


quickest_concat('caution', ['ion', 'caut', 'caution']) # -> 1


quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']) # -> 4


quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']) # -> 3


quickest_concat('simchacindy', ['sim', 'simcha', 'acindy']) # -> -1


quickest_concat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']) # -> 2


quickest_concat('rongbetty', ['wrong', 'bet']) # -> -1


quickest_concat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']) # -> 7
