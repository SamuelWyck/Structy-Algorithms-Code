"""Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value1(head, index):
  value = None
  position = 0
  while head is not None:
    if position == index:
      value = head.val
      break
    else:
      position += 1
      head = head.next
  return value

def get_node_value(head, index):
  if head is None:
    return None
  elif index == 0:
    return head.val
  return get_node_value(head.next, index - 1)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d

get_node_value(a, 2) # 'c'


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d

get_node_value(a, 3) # 'd'


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d

get_node_value(a, 3) # 'd'


node1 = Node("banana")
node2 = Node("mango")
node1.next = node2
# banana -> mango

get_node_value(node1, 0) # 'banana'


node1 = Node("banana")
node2 = Node("mango")
node1.next = node2
# banana -> mango

get_node_value(node1, 1) # 'mango'


