"""Write a function, string_search, that takes in a grid of letters and a string as arguments. The function should return a boolean indicating whether or not the string can be found in the grid as a path by connecting horizontal or vertical positions. The path can begin at any position, but you cannot reuse a position more than once in the path.

You can assume that all letters are lowercase and alphabetic."""

def string_search2(grid, s):
  letter_hash = make_letter_hash(s)
  stack = []
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] in letter_hash:
        temp_hash = letter_hash.copy()
        stack.append((r, c))
        visited.add((r, c))
        while stack:
          row, col = stack.pop()
          temp_hash[grid[row][col]] -= 1

          neighbors = [
            (row - 1, col), (row + 1, col),
            (row, col - 1), (row, col + 1)]

          for neighbor in neighbors:
            if 0 <= neighbor[0] < len(grid):
              if 0 <= neighbor[1] < len(grid[0]):
                if neighbor not in visited:
                  letter = grid[neighbor[0]][neighbor[1]]
                  if letter in temp_hash:
                    if temp_hash[letter] > 0:
                      stack.append(neighbor)
                      visited.add(neighbor)
                    
        word_found = True
        for letter in temp_hash:
          if temp_hash[letter] > 0:
            word_found = False
        if word_found:
          return True
        else:
          visited.clear()
  return False


def make_letter_hash(string):
  hash = {}
  for char in string:
    if char not in hash:
      hash[char] = 1
    else:
      hash[char] += 1
  return hash



def string_search1(grid, s):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if dfs(grid, r, c, s, set()):
        return True
  return False


def dfs(grid, r, c, s, visited):
  if s == "":
    return True
  if (r, c) in visited:
    return False
  visited.add((r, c))
  if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
    return False
  if grid[r][c] != s[0]:
    return False

  part = s[1:]
  neighbors = [
    (r - 1, c), (r + 1, c),
    (r, c - 1), (r, c + 1)]
  for neighbor in neighbors:
    if dfs(grid, neighbor[0], neighbor[1], part, set(visited)):
      return True
  return False



def string_search(grid, s):
  stack = []
  visited = set()
  i = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == s[0]:
        stack.append((r, c))
        visited.add((r, c))
        while stack:
          row, col = stack.pop()
          if grid[row][col] == s[i]:
            i += 1
            if i == len(s):
              return True
    
          neighbors = [
            (row - 1, col), (row + 1, col),
            (row, col - 1), (row, col + 1)]

          for neighbor in neighbors:
            if 0 <= neighbor[0] < len(grid):
              if 0 <= neighbor[1] < len(grid[0]):
                if neighbor not in visited:
                  if grid[neighbor[0]][neighbor[1]] == s[i]:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    
        i = 0
        visited.clear()
  return False


grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'hello') # -> True


grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'proxy') # -> True


grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'rolling') # -> False


grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'z', 'm']
]
string_search(grid, 'zoo') # -> False


grid = [
  ['q', 'w', 'h', 'i', 'j'],
  ['q', 'e', 'r', 'o', 'p'],
  ['h', 'y', 't', 'x', 'z'],
  ['k', 'o', 'm', 'o', 'p']
]
string_search(grid, 'qwerty') # -> True


grid = [ 
  [ 'f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p' ], 
  [ 'o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v' ], 
  [ 'g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n' ], 
  [ 'a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm' ], 
  [ 'm', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c' ], 
  [ 'q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z' ], 
  [ 'd', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k' ], 
  [ 'f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w' ], 
  [ 'p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i' ], 
  [ 'l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q' ] 
]
string_search(grid, 'paprika') # -> True


grid = [
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h' ],
]
string_search(grid, 'ssssssssssh') # -> False


grid = [
  ['a', 'b', 'a'],
  ['t', 'x', 'x'],
  ['x', 'x', 'x'],
];
string_search(grid, 'abat') # -> true
