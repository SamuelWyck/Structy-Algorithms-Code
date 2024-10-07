"""Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def tree_includes1(root, target):
  if root is None:
    return False
  stack = [root]
  while stack:
    node = stack.pop()
    if node.val == target:
      return True
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return False


def tree_includes2(root, target):
  if root is None:
    return False
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node.val == target:
      return True
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
  return False


def tree_includes(root, target):
  if root is None:
    return False
  if root.val == target:
    return True
  left_side = tree_includes(root.left, target)
  right_side = tree_includes(root.right, target)
  if left_side:
    return True
  elif right_side:
    return True
  else:
    return False


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
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

tree_includes(a, "e") # -> True


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
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

tree_includes(a, "e") # -> True


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
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

tree_includes(a, "n") # -> False


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

tree_includes(a, "f") # -> True


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

tree_includes(a, "p") # -> False


tree_includes(None, "b") # -> False
