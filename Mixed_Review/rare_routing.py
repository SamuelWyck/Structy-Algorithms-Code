"""Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples where each tuple represents a direct road that connects a pair of cities. The function should return a boolean indicating whether or not there exists a unique route for every pair of cities. A route is a sequence of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means if there is a road between A and B, then you can use that road to go from A to B or go from B to A.

For example, given these roads:

0 --- 1
| \
|  \
|   \
2    3

There is a unique route for between every pair of cities.
So the answer is True.


For example, given these roads:

0 --- 1
| \
|  \
|   \
2 -- 3

There are two routes that can be used to travel from city 1 to city 2:
- first route:  1, 0, 2
- second route: 1, 0, 3, 2 
The answer is False, because routes should be unique."""

def rare_routing1(n, roads):
  graph = make_graph(roads)
  visited = set()
  islands = 0
  stack = []
  last_node = None
  for node in graph:
    if node not in visited:
      if islands == 1:
        return False
      islands += 1
      stack.append((node, None))
      while stack:
        node, last_node = stack.pop()
        if node in visited:
          return False
        else:
          visited.add(node)
        for neighbor in graph[node]:
          if neighbor != last_node:
            stack.append((neighbor, node))
  return True



def rare_routing(n, roads):
  graph = make_graph(roads)
  visited = set()
  stack = [(0, None)]
  last_node = None
  while stack:
    node, last_node = stack.pop()
    if node in visited:
      return False
    else:
      visited.add(node)
    for neighbor in graph[node]:
      if neighbor != last_node:
        stack.append((neighbor, node))
  if len(visited) != n:
    return False
  return True


def make_graph(edges):
  graph = {}
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = [edge[1]]
    else:
      graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
      graph[edge[1]] = [edge[0]]
    else:
      graph[edge[1]].append(edge[0])
  return graph


rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
]) # -> True


rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3),
  (3, 2)
]) # -> False


rare_routing(6, [
  (1, 2),
  (5, 4),
  (3, 0),
  (0, 1),
  (0, 4),
]) # -> True


rare_routing(6, [
  (1, 2),
  (4, 1),
  (5, 4),
  (3, 0),
  (0, 1),
  (0, 4),
]) # -> False


rare_routing(4, [
  (0, 1),
  (3, 2),
]) # -> False


rare_routing(4, [
  (0, 1),
  (0, 2),
  (1, 2)
]) # -> False
