"""Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1. You can assume that A and B exist as nodes in the graph."""

from collections import deque

def make_graph(edges):
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
  return graph


def shortest_path(edges, node_A, node_B):
  graph = make_graph(edges)
  visited = set()
  queue = deque([(node_A, 0)])
  while queue:
    node = queue.popleft()
    if node[0] == node_B:
      return node[1]
    visited.add(node[0])
    for neighbor in graph[node[0]]:
      if neighbor not in visited:
        queue.append((neighbor, node[1] + 1))
  return -1


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2


edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'a', 'e') # -> 3


edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'e', 'c') # -> 2


edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'b', 'g') # -> -1


edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

shortest_path(edges, 'w', 'e') # -> 1


edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

shortest_path(edges, 'n', 'e') # -> 2


edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

shortest_path(edges, 'm', 's') # -> 6
