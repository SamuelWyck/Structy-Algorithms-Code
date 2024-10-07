"""Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.

You may assume that the input tree is non-empty."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque


def bottom_right_value1(root):
  if root.left is None and root.right is None:
    return root.val
  value = None
  max_distance = 0
  stack = [(root, 0)]
  while stack:
    node, distance = stack.pop()
    if distance >= max_distance:
      max_distance = distance
      if node.right is not None:
        value = node.right.val
      elif node.left is not None:
        value = node.left.val
    if node.left is not None:
      stack.append((node.left, distance + 1))
    if node.right is not None:
      stack.append((node.right, distance + 1))
  return value


def bottom_right_value2(root):
  max_distance = -1
  value = None
  queue = deque([(root, 0)])
  while queue:
    node, distance = queue.popleft()
    if distance > max_distance:
      max_distance = distance
      value = node.val
    if node.right is not None:
      queue.append((node.right, distance + 1))
    if node.left is not None:
      queue.append((node.left, distance + 1))
  return value


def bottom_right_value(root):
  queue = deque([root])
  value = None
  while queue:
    node = queue.popleft()
    value = node.val
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
  return value


a = Node(3)
b = Node(11)
c = Node(10)
d = Node(4)
e = Node(-2)
f = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

bottom_right_value(a) # -> 1


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \       
#    -2  6

bottom_right_value(a) # -> 6


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)
i = Node(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \    /   
#    -2  6  7 

bottom_right_value(a) # -> 7


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.right = d
d.left = e
e.right = f
#      a
#    /   \ 
#   b     c
#    \
#     d
#    /
#   e
#   \
#    f
          
bottom_right_value(a) # -> 'f'


a = Node(42)
#      42

bottom_right_value(a) # -> 42
