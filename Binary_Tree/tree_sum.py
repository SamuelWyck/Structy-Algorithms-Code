"""Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree."""

class Node:
  def __init__(self, val):
  self.val = val
  self.left = None
  self.right = None

from collections import deque

#depth first
def tree_sum(root):
  sum = 0
  if root is None:
    return sum
  stack = [root]
  while stack:
    node = stack.pop()
    sum += node.val
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return sum


#breadth first
def tree_sum2(root):
  sum = 0
  if root is None:
    return sum
  queue = deque([root])
  while queue:
    node = queue.popleft()
    sum += node.val
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
  return sum


#recursive depth first
def tree_sum3(root):
  if root is None:
    return 0
  left_sum = tree_sum(root.left)
  right_sum = tree_sum(root.right)
  return root.val + left_sum + right_sum


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

tree_sum(a) # -> 21


a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h
#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

tree_sum(a) # -> 10


tree_sum(None) # -> 0

