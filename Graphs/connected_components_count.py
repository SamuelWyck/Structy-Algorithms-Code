"""Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph."""

from collections import deque

def connected_components_count1(graph):
  visited = set()
  stack = []
  component_count = 0
  for node in graph:
    if node not in visited:
      stack.append(node)
      component_count += 1
      while stack:
        current = stack.pop()
        visited.add(current)
        for neighbor in graph[current]:
          if neighbor not in visited:
            stack.append(neighbor)
  return component_count


def connected_components_count(graph):
  visited = set()
  queue = deque([])
  component_count = 0
  for node in graph:
    if node not in visited:
      queue.append(node)
      component_count += 1
      while queue:
        current = queue.popleft()
        visited.add(current)
        for neighbor in graph[current]:
          if neighbor not in visited:
            queue.append(neighbor)
  return component_count


connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2


connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 1


connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 3


connected_components_count({}) # -> 0


connected_components_count({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 5
