"""Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list1(head):
  sum = 0
  while head is not None:
    sum += head.val
    head = head.next
  return sum

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

sum_list(a) # 19


x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

sum_list(x) # 42


z = Node(100)

# 100

sum_list(z) # 100


sum_list(None) # 0
