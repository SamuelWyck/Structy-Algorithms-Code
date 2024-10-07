"""Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes."""

def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0

  for node in graph:
    find_distance(graph, node, distance)
  return max(distance.values())


def find_distance(graph, node, distance):
  if node in distance:
    return distance[node]

  max_length = 0
  for neighbor in graph[node]:
    length = find_distance(graph, neighbor, distance)
    if length > max_length:
      max_length = length

  distance[node] = 1 + max_length
  return 1 + max_length


graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2


graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

longest_path(graph) # -> 4


graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}

longest_path(graph) # -> 2


graph = {
  'a': ['b'],
  'b': ['c'],
  'c': [],
  'e': ['f'],
  'f': ['g'],
  'g': ['h'],
  'h': []
}

longest_path(graph) # -> 3


graph = {
  'a': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'b': ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'c': ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'd': ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'e': ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'f': ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'g': ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'h': ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'i': ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'j': ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
  'k': ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
  'l': ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'm': ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
  'n': ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
  'o': ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
  'p': ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'q': ['r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'r': ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
  's': ['t', 'u', 'v', 'w', 'x', 'y', 'z'],
  't': ['u', 'v', 'w', 'x', 'y', 'z'],
  'u': ['v', 'w', 'x', 'y', 'z'],
  'v': ['w', 'x', 'y', 'z'],
  'w': ['x', 'y', 'z'],
  'x': ['y', 'z'],
  'y': ['z'],
  'z': []
}

longest_path(graph) # -> 25
