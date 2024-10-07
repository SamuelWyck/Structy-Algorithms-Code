"""Write a function, build_tree_in_post, that takes in a list of in-ordered values and a list of post-ordered values for a binary tree. The function should build a binary tree that has the given in-order and post-order traversal structure. The function should return the root of this tree.

You can assume that the values of inorder and postorder are unique."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  if not in_order and not post_order:
    return None

  root = Node(post_order[-1])
  idx = in_order.index(post_order[-1])
  root.left = build_tree_in_post(in_order[:idx], post_order[:idx])
  root.right = build_tree_in_post(in_order[idx + 1:], post_order[idx:-1])
  return root


build_tree_in_post(
  [ 'y', 'x', 'z' ],
  [ 'y', 'z', 'x' ] 
)
#       x
#    /    \
#   y      z


build_tree_in_post(
  [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
  [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
)
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g


build_tree_in_post(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
)
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h


build_tree_in_post(
  ['m', 'n'],
  ['m', 'n']
)
#       n
#     /
#    m


build_tree_in_post(
  ['n', 'm'],
  ['m', 'n']
)
#     n
#      \
#       m
