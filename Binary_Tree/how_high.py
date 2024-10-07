"""Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def how_high1(root):
  if root is None:
    return -1
  max_edges = 0
  stack = [(root, 0)]
  while stack:
    node, distance = stack.pop()
    if distance > max_edges:
      max_edges = distance
    if node.right is not None:
      stack.append((node.right, distance + 1))
    if node.left is not None:
      stack.append((node.left, distance + 1))
  return max_edges


def how_high2(root):
  if root is None:
    return -1
  max_edges = 0
  queue = deque([(root, 0)])
  while queue:
    node, distance = queue.popleft()
    if distance > max_edges:
      max_edges = distance
    if node.right is not None:
      queue.append((node.right, distance + 1))
    if node.left is not None:
      queue.append((node.left, distance + 1))
  return max_edges


def how_high(root):
  if root is None:
    return -1
  return 1 + max(how_high(root.right), how_high(root.left))


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

how_high(a) # -> 2


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

how_high(a) # -> 3


a = Node('a')
c = Node('c')
a.right = c
#      a
#       \
#        c

how_high(a) # -> 1


a = Node('a')
#      a

how_high(a) # -> 0


how_high(None) # -> -1
