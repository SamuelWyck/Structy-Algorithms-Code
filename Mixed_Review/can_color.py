"""Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph. The function should return a boolean indicating whether or not it is possible to color nodes of the graph using two colors in such a way that adjacent nodes are always different colors.

For example, given this graph:

x-y-z

It is possible to color the nodes by using red for x and z, 
then use blue for y. So the answer is True.

For example, given this graph:

    q
   / \
  s - r

It is not possible to color the nodes without making two 
adjacent nodes the same color. So the answer is False."""

def can_color1(graph):
  stack = []
  visited = {}
  for node in graph:
    if node in visited:
      stack.append((node, visited[node]))
    else:
      stack.append((node, True))
    while stack:
      node, bool = stack.pop()
      if node in visited:
        if visited[node] != bool:
          return False
      else:
        visited[node] = bool
      for neighbor in graph[node]:
        if neighbor not in visited:
          stack.append((neighbor, bool == False))
          visited[neighbor] = bool == False
  return True



def can_color(graph):
  coloring = {}
  for node in graph:
    if node not in coloring and not validate(graph, node, coloring, False):
      return False
  return True


def validate(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]

  coloring[node] = current_color
  for neighbor in graph[node]:
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False
  return True


can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
}) # -> True


can_color({
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
}) # -> False


can_color({
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
}) # -> False


can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a", "d"],
  "d": ["a", "c"],
}) # -> False


can_color({
  "h": ["i", "k"],
  "i": ["h", "j"],
  "j": ["i", "k"],
  "k": ["h", "j"],
}) # -> True


can_color({
  "z": []
}) # -> True



can_color({
  "h": ["i", "k"],
  "i": ["h", "j"],
  "j": ["i", "k"],
  "k": ["h", "j"],
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
}) # -> False


can_color({ 
  "a": ["b", "d"], 
  "c": ["b", "f"], 
  "b": ["a", "c"], 
  "d": ["a", "e"], 
  "e": ["d", "f"], 
  "f": ["e", "c"]
}) # -> True


can_color({
  "a": ["b"],
  "d": ["c"],
  "b": ["a", "c"],
  "c": ["b", "d"]
}) # -> True
