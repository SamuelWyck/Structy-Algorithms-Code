"""Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses."""

def make_graph(edges):
  graph = {}
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = [edge[1]]
    else:
      graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
      graph[edge[1]] = []
  return graph


def prereqs_possible(num_courses, prereqs):
  graph = make_graph(prereqs)
  visiting = set()
  visited = set()
  stack = []
  first_pass = True
  for node in graph:
    if has_cycle(graph, node, visiting, visited):
      return False
  return True


def has_cycle(graph, node, visiting, visited):
  if node in visited:
    return False
  if node in visiting:
    return True

  visiting.add(node)
  for neighbor in graph[node]:
    if has_cycle(graph, neighbor, visiting, visited):
      return True
  visiting.remove(node)
  visited.add(node)
  return False


numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs) # -> True


numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
prereqs_possible(numCourses, prereqs) # -> False


numCourses = 5
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]
prereqs_possible(numCourses, prereqs) # -> True


numCourses = 5
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]
prereqs_possible(numCourses, prereqs) # -> True


numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> True


numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (7, 4),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> False


numCourses = 42
prereqs = [(6, 36)]
prereqs_possible(numCourses, prereqs) # -> True
