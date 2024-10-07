"""Write a function, flip_tree, that takes in the root of a binary tree. The function should flip the binary tree, turning left subtrees into right subtrees and vice-versa. This flipping should occur in-place by modifying the original tree. The function should return the root of the tree."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def flip_tree1(root):
  stack = [root]
  while stack:
    node = stack.pop()
    left = node.left
    node.left = node.right
    node.right = left
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return root


def flip_tree(root):
  return _flip_tree(root, root)


def _flip_tree(root, head):
  if root is None:
    return head

  left = root.left
  root.left = root.right
  root.right = left
  _flip_tree(root.left, head)
  _flip_tree(root.right, head)
  return head


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
e.right = h
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

flip_tree(a) 
#       a
#    /    \
#   c      b
#  /     /   \
# f     e    d
#     /  \
#    h    g


u = Node("u")
t = Node("t")
s = Node("s")
r = Node("r")
q = Node("q")
p = Node("p")
u.left = t
u.right = s
s.right = r
r.left = q
r.right = p
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p

flip_tree(u)
#           u
#        /    \
#       s      t
#      /
#     r
#    / \
#   p  q


l = Node("l")
m = Node("m")
n = Node("n")
o = Node("o")
p = Node("p")
q = Node("q")
r = Node("r")
s = Node("s")
t = Node("t")
l.left = m
l.right = n
n.left = o
n.right = p
o.left = q
o.right = r
p.left = s
p.right = t
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t

flip_tree(l)
#             l
#         /      \
#        n        m
#      /  \
#    p     o
#  / \    / \
# t   s  r   q


n = Node("n")
y = Node("y")
c = Node("c")
n.left = y
n.right = c
#       n
#     /   \
#    y     c

flip_tree(n)
#       n
#     /   \
#    c     y
