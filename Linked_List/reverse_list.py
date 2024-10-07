"""Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list1(head):
  min_index = 0
  max_index = 0
  node = head
  while node.next is not None:
    max_index += 1
    node = node.next

  while min_index < max_index:
    index = 0
    temp = 0
    node1 = head
    while index < max_index:
      node1 = node1.next
      index += 1
    index = 0
    node2 = head
    while index < min_index:
      node2 = node2.next
      index += 1
    temp = node2.val
    node2.val = node1.val
    node1.val = temp
    max_index -= 1
    min_index += 1
  return head
    
def reverse_list2(head):
  prev = None
  current = head
  next = head.next
  while next is not None:
    current.next = prev
    prev = current
    current = next
    next = current.next
  current.next = prev
  return current

def reverse_list4(head, prev=None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)

def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c -> d -> e -> f

reverse_list(a) # f -> e -> d -> c -> b -> a


x = Node("x")
y = Node("y")
x.next = y
# x -> y

reverse_list(x) # y -> x


p = Node("p")
# p

reverse_list(p) # p


