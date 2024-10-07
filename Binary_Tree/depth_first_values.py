"""Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values1(root):
  visited = []
  if root is None:
    return visited
  stack = [root]
  while len(stack) > 0:
    node = stack.pop()
    visited.append(node.val)
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return visited


def depth_first_values(root):
  if root is None:
    return []
  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [root.val, *left_values, *right_values]


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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']


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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']


a = Node('a')
#     a
depth_first_values(a) 
#   -> ['a']


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b;
b.left = c;
c.right = d;
d.right = e;
#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

depth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e']


depth_first_values(None) 
#   -> []


