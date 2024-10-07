"""Write a function, linked_palindrome, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list is a palindrome. A palindrome is a sequence that is the same both forwards and backwards."""

class Node:
  def __init__(self, val):
  self.val = val
  self.next = None

def linked_palindrome1(head):
  if head is None:
    return True
  first_values = ""
  second_values = ""
  current = head
  while current is not None:
    first_values += str(current.val)
    current = current.next

  current = head
  next = current.next
  prev = None
  while next is not None:
    current.next = prev
    prev = current
    current = next
    next = current.next
  current.next = prev
  
  while current is not None:
    second_values += str(current.val)
    current = current.next
  if first_values == second_values:
    return True
  return False


def linked_palindrome(head):
  if head is None:
    return True
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next

  if values == values[::-1]:
    return True
  return False


a = Node(3)
b = Node(2)
c = Node(7)
d = Node(7)
e = Node(2)
f = Node(3)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 3 -> 2 -> 7 -> 7 -> 2 -> 3

linked_palindrome(a) # True


a = Node(3)
b = Node(2)
c = Node(4)
a.next = b
b.next = c
# 3 -> 2 -> 4

linked_palindrome(a) # False


a = Node(3)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
# 3 -> 2 -> 3

linked_palindrome(a) # True


a = Node(0)
b = Node(1)
c = Node(0)
d = Node(1)
e = Node(0)
a.next = b
b.next = c
c.next = d
d.next = e
# 0 -> 1 -> 0 -> 1 -> 0

linked_palindrome(a) # True


a = Node(0)
b = Node(1)
c = Node(0)
d = Node(1)
e = Node(1)
a.next = b
b.next = c
c.next = d
d.next = e
# 0 -> 1 -> 0 -> 1 -> 1

linked_palindrome(a) # False


a = Node(5)
# 5

linked_palindrome(a) # True


linked_palindrome(None) # True


