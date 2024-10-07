"""Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list1(values):
  if not values:
    return None
  head = Node(None)
  current = head
  for value in values:
    current.next = Node(value)
    current = current.next
  return head.next


def create_linked_list2(values):
  if not values:
    return None
  value = values.pop(0)
  head = Node(value)
  head.next = create_linked_list(values)
  return head


def create_linked_list(values, i=0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head


create_linked_list(["h", "e", "y"])
# h -> e -> y


create_linked_list([1, 7, 1, 8])
# 1 -> 7 -> 1 -> 8


create_linked_list(["a"])
# a


create_linked_list([])
# null

