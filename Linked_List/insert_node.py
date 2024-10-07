"""Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the length of the input list."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node1(head, value, index):
  if index == 0:
    node = Node(value)
    node.next = head
    return node
  list_index = 0
  current = head
  prev = None
  while current is not None:
    if list_index == index:
      node = Node(value)
      prev.next = node 
      node.next = current
      break 
    prev = current
    current = current.next
    list_index += 1
  if current is None:
    prev.next = Node(value)
  return head


def insert_node2(head, value, index):
  if index == 0:
    node = Node(value)
    node.next = head
    return node
  list_index = 0
  current = head
  while current is not None:
    if index - list_index == 1:
      next = current.next
      node = Node(value)
      current.next = node
      node.next = next
      break
    current = current.next
    list_index += 1
  return head


def insert_node(head, value, index, count=0):
  if index == 0:
    node = Node(value)
    node.next = head
    return node
  if head is None:
    return None
  if count == index - 1:
    next = head.next
    node = Node(value)
    head.next = node
    node.next = next
    return  
  insert_node(head.next, value, index, count + 1)
  return head


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d

insert_node(a, 'x', 2)
# a -> b -> x -> c -> d


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d

insert_node(a, 'v', 3)
# a -> b -> c -> v -> d


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d

insert_node(a, 'm', 4)
# a -> b -> c -> d -> m


a = Node("a")
b = Node("b")
a.next = b
# a -> b

insert_node(a, 'z', 0)
# z -> a -> b



