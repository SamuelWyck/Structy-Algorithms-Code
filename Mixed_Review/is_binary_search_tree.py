"""Write a function, is_binary_search_tree, that takes in the root of a binary tree. The function should return a boolean indicating whether or not the tree satisfies the binary search tree property.

A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value and all values in a node's right subtree are greater than or equal to the node's value."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def is_binary_search_tree1(root):
  max_left = find_max(root.left)
  min_right = find_min(root.right)
  if max_left < root.val and min_right > root.val:
    return True
  return False


def find_max(root):
  max_value = float("-inf")
  stack = [root]
  while stack:
    node = stack.pop()
    max_value = max(max_value, node.val)
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return max_value


def find_min(root):
  min_value = float("inf")
  stack = [root]
  while stack:
    node = stack.pop()
    min_value = min(min_value, node.val)
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return min_value



def is_binary_search_tree(root):
  values = []
  _is_binary_search_tree(root, values)
  for i in range(len(values) - 1):
    if values[i] > values[i + 1]:
      return False
  return True


def _is_binary_search_tree(root, values):
  if root is None:
    return
  _is_binary_search_tree(root.left, values)
  values.append(root.val)
  _is_binary_search_tree(root.right, values)


a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(9)
f = Node(19)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19

is_binary_search_tree(a) # -> True


a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(15)
f = Node(19)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      12
#    /   \
#   5     18
#  / \     \
# 3   15     19

is_binary_search_tree(a) # -> False


a = Node(12)
b = Node(5)
c = Node(19)
d = Node(3)
e = Node(9)
f = Node(19)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      12
#    /   \
#   5     19
#  / \     \
# 3   9     19

is_binary_search_tree(a) # -> True


a = Node(12)
b = Node(5)
c = Node(10)
d = Node(3)
e = Node(9)
f = Node(19)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      12
#    /   \
#   5     10
#  / \     \
# 3   9     19

is_binary_search_tree(a) # -> False


q = Node(54)
r = Node(42)
s = Node(70)
t = Node(31)
u = Node(50)
v = Node(72)
w = Node(47)
x = Node(90)
q.left = r
q.right = s
r.left = t
r.right = u
s.right = v
u.left = w
v.right = x
#       54
#     /    \
#    42     70
#   / \      \
# 31   50     72
#     /        \
#    47         90

is_binary_search_tree(q) # -> True
