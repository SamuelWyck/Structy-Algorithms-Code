"""Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island."""

from collections import deque

def minimum_island(grid):
  visited = set()
  queue = deque([])
  smallest_island = float('inf')
  row_index = 0
  col_index = 0
  for row in grid:
    col_index = 0
    for position in row:
      if position == "L":
        if (row_index, col_index) not in visited:
          queue.append((row_index, col_index))
          visited.add((row_index, col_index))
          island_size = 0
          while queue:
            row, col = queue.popleft()
            island_size += 1
            neighbors = [
              (row -1, col), (row + 1, col),
              (row, col -1), (row, col + 1)]
            for neighbor in neighbors:
              if neighbor not in visited:
                if neighbor[0] >= 0 and neighbor[1] >= 0:
                  try:
                    pos = grid[neighbor[0]][neighbor[1]]
                    if pos == "L":
                      queue.append(neighbor)
                      visited.add(neighbor)
                  except IndexError:
                    pass
          if island_size < smallest_island:
            smallest_island = island_size
      col_index += 1
    row_index += 1
  return smallest_island


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2


grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

minimum_island(grid) # -> 1


grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

minimum_island(grid) # -> 9


grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

minimum_island(grid) # -> 1
