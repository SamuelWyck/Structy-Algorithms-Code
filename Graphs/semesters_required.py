"""Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses."""

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


def semesters_required(num_courses, prereqs):
  graph = make_graph(prereqs)
  if len(graph) == 0:
    return 1
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 1

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
  return distance[node]


num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
semesters_required(num_courses, prereqs) # -> 3


num_courses = 7
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
semesters_required(num_courses, prereqs) # -> 5


num_courses = 5
prereqs = [
  (1, 0),
  (3, 4),
  (1, 2),
  (3, 2),
]
semesters_required(num_courses, prereqs) # -> 2


num_courses = 12
prereqs = []
semesters_required(num_courses, prereqs) # -> 1


num_courses = 3
prereqs = [
  (0, 2),
  (0, 1),
  (1, 2),
]
semesters_required(num_courses, prereqs) # -> 3


num_courses = 6
prereqs = [
  (3, 4),
  (3, 0),
  (3, 1),
  (3, 2),
  (3, 5),
]
semesters_required(num_courses, prereqs) # -> 2
