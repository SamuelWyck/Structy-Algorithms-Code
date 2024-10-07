"""Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes."""

from collections import deque

def has_path1(graph, src, dst):
  if graph is None or src is None or dst is None:
    return False
  stack = [src]
  while len(stack) > 0:
    node = stack.pop()
    if node == dst:
      return True
    for neighbor in graph[node]:
      stack.append(neighbor)
  return False


def has_path1(graph, src, dst):
  if graph is None or src is None or dst is None:
    return False
  queue = deque([src])
  while queue:
    node = queue.popleft()
    if node == dst:
      return True
    for neighbor in graph[node]:
      queue.append(neighbor)
  return False


def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'k') # True


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'j') # False


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'i', 'h') # True


graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'w') # True


graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'z') # False
