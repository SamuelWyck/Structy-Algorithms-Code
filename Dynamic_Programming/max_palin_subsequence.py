"""Write a function, max_palin_subsequence, that takes in a string as an argument. The function should return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters."""

def max_palin_subsequence1(string):
  return _max_palin_subsequence(string, {})


def _max_palin_subsequence1(string, memo):
  if string in memo:
    return memo[string]
  if len(string) == 0:
    return 0
  if len(string) == 1:
    return 1
    
  length = 0 
  if string[0] == string[-1]:
    length += 2 + _max_palin_subsequence(string[1:-1], memo)
  else:
    left = _max_palin_subsequence(string[1:], memo)
    right = _max_palin_subsequence(string[:-1], memo)
    length += max(left, right)
    
  memo[string] = length
  return memo[string]
    
    
    
def max_palin_subsequence(string):
  return _max_palin_subsequence(string, {}, 0, len(string) - 1)


def _max_palin_subsequence(string, memo, start, end):
  if (start, end) in memo:
    return memo[(start, end)]
  if start > end:
    return 0
  if start == end:
    return 1
    
  length = 0 
  if string[start] == string[end]:
    length += 2 + _max_palin_subsequence(string, memo, start + 1, end - 1)
  else:
    left = _max_palin_subsequence(string, memo, start + 1, end)
    right = _max_palin_subsequence(string, memo, start, end - 1)
    length += max(left, right)
    
  memo[(start, end)] = length
  return memo[(start, end)]


max_palin_subsequence("luwxult") # -> 5


max_palin_subsequence("xyzaxxzy") # -> 6


max_palin_subsequence("lol") # -> 3


max_palin_subsequence("z") # -> 1


max_palin_subsequence("chartreusepugvicefree") # -> 7


max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15


max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31
