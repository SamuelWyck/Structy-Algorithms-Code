"""Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land."""

def island_count(grid):
  visited = set()
  stack = []
  island_count = 0
  row_index = 0
  col_index = 0
  for row in grid:
    col_index = 0
    for position in row:
      if position == "L":
        if (row_index, col_index) not in visited:
          stack.append((row_index, col_index))
          island_count += 1
          while stack:
            row, col = stack.pop()
            visited.add((row, col))
            neighbors = [
              (row - 1, col), (row + 1, col),
              (row, col - 1), (row, col + 1)] 
            for neighbor in neighbors:
              if neighbor not in visited:
                try:
                  pos = grid[neighbor[0]][neighbor[1]]
                  if pos == "L":
                    stack.append(neighbor)
                except IndexError:
                  pass
      col_index += 1
    row_index += 1
  return island_count


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3


grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

island_count(grid) # -> 4


grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

island_count(grid) # -> 1


grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

island_count(grid) # -> 0
