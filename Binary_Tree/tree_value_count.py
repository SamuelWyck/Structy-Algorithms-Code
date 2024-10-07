"""Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def tree_value_count1(root, target):
  if root is None:
    return 0
  target_count = 0
  stack = [root]
  while stack:
    node = stack.pop()
    if node.val == target:
      target_count += 1
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return target_count


def tree_value_count2(root, target):
  if root is None:
    return 0
  target_count = 0
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node.val == target:
      target_count += 1
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
  return target_count


def tree_value_count(root, target):
  count = 0
  if root is None:
    return 0
  if root.val == target:
    count += 1

  count += tree_value_count(root.left, target) + tree_value_count(root.right, target)
  return count


a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

tree_value_count(a,  6) # -> 3


a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      12
#    /   \
#   6     6
#  / \     \
# 4  6     12

tree_value_count(a,  12) # -> 2


a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h
#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

tree_value_count(a, 1) # -> 4


a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h
#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

tree_value_count(a, 9) # -> 0


tree_value_count(None, 42) # -> 0

