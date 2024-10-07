"""Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. The function should return a string representing the combination."""

def safe_cracking(hints):
  graph = make_graph(hints)
  parent_hash = make_parent_hash(graph)

  combo = []
  stack = [node for node in parent_hash if parent_hash[node] == 0]

  while stack:
    node = stack.pop()
    combo.append(str(node))

    for child in graph[node]:
      parent_hash[child] -= 1
      if parent_hash[child] == 0:
        stack.append(child)
        
  return "".join(combo)


def make_parent_hash(graph):
  hash = {}
  for node in graph:
    if node not in hash:
      hash[node] = 0
    else:
      hash[node] += 1
    for child in graph[node]:
      if child not in hash:
        hash[child] = 0
      else:
        hash[child] += 1
  return hash


def make_graph(edges):
  graph = {}
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = [edge[1]]
    else:
      graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
      graph[edge[1]] = []
  return graph


safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
]) # -> '718'


safe_cracking([
  (3, 1),
  (4, 7),
  (5, 9),
  (4, 3),
  (7, 3),
  (3, 5),
  (9, 1),
]) # -> '473591'


safe_cracking([
  (2, 5),
  (8, 6),
  (0, 6),
  (6, 2),
  (0, 8),
  (2, 3),
  (3, 5),
  (6, 5),
]) # -> '086235'


safe_cracking([
  (0, 1),
  (6, 0),
  (1, 8),
]) # -> '6018'


safe_cracking([
  (8, 9),
  (4, 2),
  (8, 2),
  (3, 8),
  (2, 9),
  (4, 9),
  (8, 4),
]) # -> '38429'
