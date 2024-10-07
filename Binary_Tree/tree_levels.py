"""Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def tree_levels1(root):
  paths = []
  if root is None:
    return paths
  max_distance = -1
  queue = deque([(root, 0)])
  while queue:
    node, distance = queue.popleft()
    if distance > max_distance:
      max_distance = distance
      paths.append([node.val])
    else:
      paths[-1].append(node.val)
    if node.left is not None:
      queue.append((node.left, distance + 1))
    if node.right is not None:
      queue.append((node.right, distance + 1))
  return paths
  

def tree_levels(root):
  levels = []
  if root is None:
    return levels
  stack = [(root, 0)]
  while stack:
    node, level = stack.pop()
    if len(levels) - 1 < level:
      levels.append([node.val])
    else:
      levels[level].append(node.val)
    if node.right is not None:
      stack.append((node.right, level + 1))
    if node.left is not None:
      stack.append((node.left, level + 1))
  return levels


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]


q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
v = Node('v')
q.left = r
q.right = s
r.right = t
t.left = u
u.right = v
#      q
#    /   \
#   r     s
#    \
#     t
#    /
#   u
#  /
# v

tree_levels(q) # ->
# [
#   ['q'],
#   ['r', 's'],
#   ['t'],
#   ['u'],
#   ['v']
# ]


tree_levels(None) # -> []
