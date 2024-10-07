"""Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def tree_min_value1(root):
  min_value = root.val
  stack = [root]
  while stack:
    node = stack.pop()
    if node.val < min_value:
      min_value = node.val
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return min_value


def tree_min_value2(root):
  min_value = root.val
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node.val < min_value:
      min_value = node.val
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
  return min_value


def tree_min_value(root, min_value=None):
  if root is None:
    return min_value
  if not min_value:
    min_value = root.val
  elif root.val < min_value:
    min_value = root.val
  left_min = tree_min_value(root.left, min_value)
  right_min = tree_min_value(root.right, min_value)
  if left_min <= right_min:
    return left_min
  else:
    return right_min


a = Node(3)
b = Node(11)
c = Node(4)
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
#   11     4
#  / \      \
# 4   -2     1

tree_min_value(a) # -> -2


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

tree_min_value(a) # -> 3


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(-2)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     /       \
#    -2       -2

tree_min_value(a) # -> -13


a = Node(42)
#        42

tree_min_value(a) # -> 42

