"""Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements."""

def intersection1(a, b):
  c = a + b
  seen = {}
  for num in c:
    if num not in seen:
      seen[num] = 1
    elif num in seen:
      seen[num] += 1
  result = []
  for item in seen:
    if seen[item] > 1:
      result.append(item)
  return result
      
def intersection(a, b):
  hm = set()
  for element in a:
    hm.add(element)
  result = []
  for element in b:
    if element in hm:
      result.append(element)
  return result

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
intersection([2,4,6], [4,2]) # -> [2,4]
intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
intersection([0,1,2], [10,11]) # -> []
intersection([0,1,2], [10,11]) # -> []
