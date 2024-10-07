"""Write a function, middle_value, that takes in the head of a linked list as an argument. The function should return the value of the middle node in the linked list. If the linked list has an even number of nodes, then return the value of the second middle node.

You may assume that the input list is non-empty."""

class Node:
  def __init__(self, val):
  self.val = val
  self.next = None

def middle_value1(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next

  return find_middle(values, 0, len(values) - 1)


def find_middle(values, start, end):
  if start > end:
    return values[start]
  if start == end:
    return values[start]

  return find_middle(values, start + 1, end - 1)



def middle_value2(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next

  return values[len(values)//2]



def middle_value(head):
  slow = head
  fast = head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  return slow.val


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e
# a -> b -> c -> d -> e

middle_value(a) # c


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c -> d -> e -> f

middle_value(a) # d


x = Node('x')
y = Node('y')
z = Node('z')
x.next = y
y.next = z
# x -> y -> z

middle_value(x) # y


x = Node('x')
y = Node('y')
x.next = y
# x -> y 

middle_value(x) # y


q = Node('q')
# q

middle_value(q) # q

