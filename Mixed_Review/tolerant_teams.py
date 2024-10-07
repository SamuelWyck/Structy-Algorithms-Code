"""Write a function, tolerant_teams, that takes in a list of rivalries as an argument. A rivalry is a pair of people who should not be placed on the same team. The function should return a boolean indicating whether or not it is possible to separate people into two teams, without rivals being on the same team. The two teams formed do not have to be the same size."""

def tolerant_teams(rivalries):
  graph = make_graph(rivalries)
  teams = {}
  for node in graph:
    if node not in teams and not validate_team(graph, node, teams, False):
      return False
  return True


def validate_team(graph, node, teams, current_team):
  if node in teams:
    return current_team == teams[node]

  teams[node] = current_team
  for neighbor in graph[node]:
    if not validate_team(graph, neighbor, teams, not current_team):
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


tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
]) # -> True


tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader'),
  ('raj', 'philip'),
  ('seb', 'raj')
]) # -> False


tolerant_teams([
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]) # -> True


tolerant_teams([
  ('alex', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]) # -> False


tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) # -> True


tolerant_teams([
  ('alan', 'jj'),
  ('jj', 'richard'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) # -> True


tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('betty', 'christine'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) # -> False


tolerant_teams([
  ['ara', 'boyka'],
  ['dennis', 'clara'],
  ['boyka', 'clara']
]) # -> True
