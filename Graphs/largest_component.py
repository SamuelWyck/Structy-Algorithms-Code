"""Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph."""

from collections import deque

def largest_component1(graph):
  largest_component = 0
  visited = set()
  stack = []
  for node in graph:
    if node not in visited:
      stack.append(node)
      component_size = 0
      while stack:
        current = stack.pop()
        if current not in visited:
          visited.add(current)
          component_size += 1
          for neighbor in graph[current]:
            if neighbor not in visited:
              stack.append(neighbor)
      if component_size > largest_component:
        largest_component = component_size
  return largest_component


def largest_component(graph):
  visited = set()
  queue = deque([])
  largest_component = 0
  for node in graph:
    if node not in visited:
      queue.append(node)
      component_size = 0
      while queue:
        current = queue.popleft()
        if current not in visited:
          visited.add(current)
          component_size += 1
          for neighbor in graph[current]:
            if neighbor not in visited:
              queue.append(neighbor)
      if component_size > largest_component:
        largest_component = component_size
  return largest_component


largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4


largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6


largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 5


largest_component({}) # -> 0


largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 3
