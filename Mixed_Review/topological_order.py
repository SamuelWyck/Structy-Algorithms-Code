"""Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph. The function should return a list containing the topological-order of the graph.

The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence."""

def topological_order(graph):
  parent_hash = make_parent_hash(graph)

  values = []
  stack = [node for node in parent_hash if parent_hash[node] == 0]

  while stack:
    node = stack.pop()
    values.append(node)
    
    for neighbor in graph[node]:
      parent_hash[neighbor] -= 1
      if parent_hash[neighbor] == 0:
        stack.append(neighbor)
  return values
  

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


topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
}) # -> ['c', 'a', 'f', 'b', 'd', 'e']


topological_order({
  "h": ["l", "m"],
  "i": ["k"],
  "j": ["k", "i"],
  "k": ["h", "m"],
  "l": ["m"],
  "m": [],
}) # -> ['j', 'i', 'k', 'h', 'l', 'm']


topological_order({
  "q": [],
  "r": ["q"],
  "s": ["r"],
  "t": ["s"],
}) # -> ['t', 's', 'r', 'q']


topological_order({
  "v": ["z", "w"],
  "w": [],
  "x": ["w", "v", "z"],
  "y": ["x"],
  "z": ["w"],
}) # -> ['y', 'x', 'v', 'z', 'w']
