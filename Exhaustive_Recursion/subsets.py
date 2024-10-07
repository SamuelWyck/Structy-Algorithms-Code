"""Write a function, subsets, that takes in a list as an argument. The function should return a 2D list where each sublist represents one of the possible subsets of the list.

The elements within the subsets and the subsets themselves may be returned in any order.

You may assume that the input list contains unique elements."""

def subsets(elements):
  if len(elements) == 0:
    return [[]]

  first = elements[0]
  subset = subsets(elements[1:])
  total = []
  for sub in subset:
    total.append([first, *sub])

  return subset + total


subsets(['a', 'b']) # ->
# [ 
#   [], 
#   [ 'b' ], 
#   [ 'a' ], 
#   [ 'a', 'b' ] 
# ]


subsets(['a', 'b', 'c']) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]


subsets(['x']) # ->
# [ 
#   [], 
#   [ 'x' ] 
# ]


subsets([]) # ->
# [ 
#   []
# ]


subsets(['q', 'r', 's', 't']) # ->
# [
#   [],
#   [ 't' ],
#   [ 's' ],
#   [ 's', 't' ],
#   [ 'r' ],
#   [ 'r', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 's', 't' ],
#   [ 'q' ],
#   [ 'q', 't' ],
#   [ 'q', 's' ],
#   [ 'q', 's', 't' ],
#   [ 'q', 'r' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 's', 't' ]
# ]
