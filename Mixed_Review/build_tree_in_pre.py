"""Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree. The function should build a binary tree that has the given in-order and pre-order traversal structure. The function should return the root of this tree.

You can assume that the values of inorder and preorder are unique."""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre1(in_order, pre_order):
  if not in_order and not pre_order:
    return None

  root = Node(pre_order[0])
  idx = in_order.index(pre_order[0])
  left_in = in_order[:idx]
  right_in = in_order[idx + 1:]
  root.left = build_tree_in_pre(left_in, pre_order[1:len(left_in) + 1])
  root.right = build_tree_in_pre(right_in, pre_order[len(left_in) + 1:])
  return root


build_tree_in_pre(
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ] 
)
#       y
#    /    \
#   z      x


build_tree_in_pre(
  [ 'y', 'z', 'x' ],
  [ 'y', 'x', 'z' ] 
)
#       y
#        \
#         x
#        / 
#       z


build_tree_in_pre(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
)
#       a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h


build_tree_in_pre(
  [ 't', 'u', 's', 'q', 'r', 'p' ],
  [ 'u', 't', 's', 'r', 'q', 'p' ] 
)
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p


build_tree_in_pre(
  [ 'm', 'l', 'q', 'o', 'r', 'n', 's', 'p', 't' ],
  [ 'l', 'm', 'n', 'o', 'q', 'r', 'p', 's', 't' ] 
)
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t
