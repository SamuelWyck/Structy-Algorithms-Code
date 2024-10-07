"""Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle."""

def has_cycle1(graph):
  visited = set()
  starting_point = None
  stack = []
  for node in graph:
    stack.append(node)
    while stack:
      node = stack.pop()
      if starting_point == None:
        starting_point = node
      elif node == starting_point:
        return True
      for neighbor in graph[node]:
        if neighbor not in visited:
          stack.append(neighbor)
          visited.add(neighbor)
    visited.clear()
    starting_point = None
  return False



def has_cycle(graph):
  visiting = set()
  visited = set()
  for node in graph:
    if cycle_detect(graph, node, visiting, visited):
      return True
  return False


def cycle_detect(graph, node, visiting, visited):
  if node in visited:
    return False
  if node in visiting:
    return True

  visiting.add(node)
  for neighbor in graph[node]:
    if cycle_detect(graph, neighbor, visiting, visited):
      return True
  visiting.remove(node)
  visited.add(node)
  return False


has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
}) # -> True


has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
}) # -> False


has_cycle({
  "a": ["b", "c"],
  "b": [],
  "c": [],
  "e": ["f"],
  "f": ["e"],
}) # -> True


has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
}) # -> False


has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
  "g": [],
}) # -> True


has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": ["b"],
}) # -> True


has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
  "e": ["c"],
}) # -> False
