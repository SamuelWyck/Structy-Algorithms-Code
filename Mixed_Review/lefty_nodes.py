"""Write a function, lefty_nodes, that takes in the root of a binary tree. The function should return a list containing the left-most value on every level of the tree. The list must be ordered in a top-down fashion where the root is the first item.

Note that the left-most node on a level may not necessarily be a left child."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def lefty_nodes(root):
  if root is None:
    return []
  queue = deque([(root, 0)])
  max_distance = -1
  left_nodes = []
  while queue:
    node, distance = queue.popleft()
    if distance > max_distance:
      left_nodes.append(node.val)
      max_distance = distance
    if node.left is not None:
      queue.append((node.left, distance + 1))
    if node.right is not None:
      queue.append((node.right, distance + 1))
  return left_nodes


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
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

lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]


u = Node('u')
t = Node('t')
s = Node('s')
r = Node('r')
q = Node('q')
p = Node('p')
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

lefty_nodes(u) # [ 'u', 't', 'r', 'q' ]


l = Node('l')
m = Node('m')
n = Node('n')
o = Node('o')
p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
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

lefty_nodes(l) # [ 'l', 'm', 'o', 'q' ]


n = Node('n')
y = Node('y')
c = Node('c')
n.left = y
n.right = c
#       n
#     /   \
#    y     c

lefty_nodes(n) # [ 'n', 'y' ]


i = Node('i')
n = Node('n')
s = Node('s')
t = Node('t')
i.right = n
n.left = s
n.right = t
#       i
#        \
#         n
#        / \
#       s   t

lefty_nodes(i) # [ 'i', 'n', 's' ]


lefty_nodes(None) # [ ]


