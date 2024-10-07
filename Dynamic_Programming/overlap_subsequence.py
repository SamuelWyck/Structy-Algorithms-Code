"""Write a function, overlap_subsequence, that takes in two strings as arguments. The function should return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters."""

def overlap_subsequence1(string_1, string_2):
  return _overlap_subsequence(
    string_1, string_2, 0, len(string_1) - 1, 0, len(string_2) - 1, {})


def _overlap_subsequence1(s1, s2, s1_s, s1_e, s2_s, s2_e, memo):
  if (s1_s, s2_s) in memo:
    return memo[(s1_s, s2_s)]
  if s1_s > s1_e or s2_s > s2_e:
    return 0

  length = 0
  if s1[s1_s] == s2[s2_s]:
    length += 1 + _overlap_subsequence(
      s1, s2, s1_s + 1, s1_e, s2_s + 1, s2_e, memo)
  else:
    left = _overlap_subsequence(s1, s2, s1_s + 1, s1_e, s2_s, s2_e, memo)
    right = _overlap_subsequence(s1, s2, s1_s, s1_e, s2_s + 1, s2_e, memo)
    length = max(left, right)

  memo[(s1_s, s2_s)] = length
  return memo[(s1_s, s2_s)]




def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})


def _overlap_subsequence(s1, s2, s1_s, s2_s, memo):
  if (s1_s, s2_s) in memo:
    return memo[(s1_s, s2_s)]
  if s1_s >= len(s1) or s2_s >= len(s2):
    return 0

  length = 0
  if s1[s1_s] == s2[s2_s]:
    length += 1 + _overlap_subsequence(s1, s2, s1_s + 1, s2_s + 1, memo)
  else:
    left = _overlap_subsequence(s1, s2, s1_s + 1, s2_s, memo)
    right = _overlap_subsequence(s1, s2, s1_s, s2_s + 1, memo)
    length = max(left, right)

  memo[(s1_s, s2_s)] = length
  return memo[(s1_s, s2_s)]


overlap_subsequence("dogs", "daogt") # -> 3


overlap_subsequence("xcyats", "criaotsi") # -> 4


overlap_subsequence("xfeqortsver", "feeeuavoeqr") # -> 5


overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") # -> 11


overlap_subsequence(
  "mumblecorebeardleggingsauthenticunicorn",
  "succulentspughumblemeditationlocavore"
) # -> 15
