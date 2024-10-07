"""Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. The function should return the value of the lowest common ancestor of the two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def lowest_common_ancestor(root, val1, val2):
  path1 = find_path2(root, val1)
  path2 = find_path2(root, val2)
  first_path = set(path1)
  for value in path2:
    if value in first_path:
      return value


def find_path(root, target):
  if root is None:
    return []
  if root.val == target:
    return [root.val]

  left = find_path(root.left, target)
  left.append(root.val)
  right = find_path(root.right, target)
  right.append(root.val)
  if left[0] == target:
    return left
  else:
    return right



def find_path2(root, target):
  if root is None:
    return None
  if root.val == target:
    return [root.val]

  left = find_path2(root.left, target)
  if left is not None:
    left.append(root.val)
    return left
  right = find_path2(root.right, target)
  if right is not None:
    right.append(root.val)
    return right

  return None


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


lowest_common_ancestor(a, 'd', 'h') # b


lowest_common_ancestor(a, 'd', 'g') # b


lowest_common_ancestor(a, 'g', 'c') # a


lowest_common_ancestor(a, 'b', 'g') # b


lowest_common_ancestor(a, 'f', 'c') # c



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


lowest_common_ancestor(l, 'r', 'p') # n


lowest_common_ancestor(l, 'm', 'o') # l


lowest_common_ancestor(l, 'm', 'o') # l


lowest_common_ancestor(l, 's', 'p') # p


