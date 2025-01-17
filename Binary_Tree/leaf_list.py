"""Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def leaf_list1(root):
  if root is None:
    return []
  leaves = []
  stack = [root]
  while stack:
    node = stack.pop()
    if node.left is None and node.right is None:
      leaves.append(node.val)
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return leaves


def leaf_list(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [root.val]
  left_leaves = leaf_list(root.left)
  right_leaves = leaf_list(root.right)
  return left_leaves + right_leaves


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

leaf_list(a) # -> [ 'd', 'e', 'f' ] 


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

leaf_list(a) # -> [ 'd', 'g', 'h' ]


a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)
a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g
#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

leaf_list(a) # -> [ 20, 1, 3, 54 ]


x = Node('x')
#      x

leaf_list(x) # -> [ 'x' ]


leaf_list(None) # -> [ ]
