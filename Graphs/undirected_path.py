"""Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B."""

from collections import deque

def undirected_path1(edges, node_A, node_B):
  stack = [node_A]
  visited = set()
  while stack:
    node = stack.pop()
    if node == node_B:
      return True
    visited.add(node)
    for edge in edges:
      if edge[0] == node:
        if edge[1] not in visited:
          stack.append(edge[1])
      elif edge[1] == node:
        if edge[0] not in visited:
          stack.append(edge[0])
  return False


def undirected_path2(edges, node_A, node_B):
  visited = set()
  queue = deque([node_A])
  while queue:
    node = queue.popleft()
    if node == node_B:
      return True
    visited.add(node)
    for edge in edges:
      if edge[0] == node:
        if edge[1] not in visited:
          queue.append(edge[1])
      elif edge[1] == node:
        if edge[0] not in visited:
          queue.append(edge[0])
  return False


def undirected_path3(edges, node_A, node_B):
  graph = {}
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = [edge[1]]
    elif edge[0] in graph:
      graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
      graph[edge[1]] = [edge[0]]
    elif edge[1] in graph:
      graph[edge[1]].append(edge[0])

  visited = set()
  stack = [node_A]
  while stack:
    node = stack.pop()
    if node == node_B:
      return True
    visited.add(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        stack.append(neighbor)
  return False


def undirected_path4(edges, node_A, node_B):
  graph = {}
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = [edge[1]]
    elif edge[0] in graph:
      graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
      graph[edge[1]] = [edge[0]]
    elif edge[1] in graph:
      graph[edge[1]].append(edge[0])

  visited = set()
  queue = deque([node_A])
  while queue:
    node = queue.popleft()
    if node == node_B:
      return True
    visited.add(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
  return False


def undirected_path(edges, node_A, node_B):
  graph = {}
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = [edge[1]]
    elif edge[0] in graph:
      graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
      graph[edge[1]] = [edge[0]]
    elif edge[1] in graph:
      graph[edge[1]].append(edge[0])

  return has_path(graph, node_A, node_B, set())


def has_path(graph, src, dst, visited):
  if src == dst:
    return True
  if src in visited:
    return False

  visited.add(src)
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
  return False


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'm', 'j') # -> True


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'l', 'j') # -> True


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'k', 'o') # -> False


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'i', 'o') # -> False


edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]


undirected_path(edges, 'a', 'b') # -> True


edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'a', 'c') # -> True


edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'r', 't') # -> True


edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'r', 'b') # -> False


edges = [
  ('s', 'r'),
  ('t', 'q'),
  ('q', 'r'),
]

undirected_path(edges, 'r', 't') # -> True
