"""Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists1(head_1, head_2):
  if head_1.val <= head_2.val:
    main = head_1
  else:
    main = head_2
  root = main
  if head_1.val == main.val:
    current1 = head_1.next
    current2 = head_2
  else:
    current1 = head_1
    current2 = head_2.next  
  while True:
    if current1.val <= current2.val:
      main.next = current1
      main = main.next
      current1 = current1.next
    elif current2.val < current1.val:
      main.next = current2
      main = main.next
      current2 = current2.next
    if current1 is None:
      main.next = current2
      break
    elif current2 is None:
      main.next = current1
      break
  return root


def merge_lists2(head_1, head_2):
  head = Node(None)
  tail = head
  current1 = head_1
  current2 = head_2
  while current1 is not None and current2 is not None:
    if current1.val <= current2.val:
      tail.next = current1
      tail = tail.next
      current1 = current1.next
    else:
      tail.next = current2
      tail = tail.next
      current2 = current2.next
  if current1 is None:
    tail.next = current2
  else:
    tail.next = current1
  return head.next


def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1

  if head_1.val < head_2.val:
    next_1 = head_1.next
    head_1.next = merge_lists(next_1, head_2)
    return head_1
  else:
    next_2 = head_2.next
    head_2.next = merge_lists(next_2, head_1)
    return head_2


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

merge_lists(a, q)
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(1)
r = Node(8)
s = Node(9)
t = Node(10)
q.next = r
r.next = s
s.next = t
# 1 -> 8 -> 9 -> 10

merge_lists(a, q)
# 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 


h = Node(30)
# 30

p = Node(15)
q = Node(67)
p.next = q
# 15 -> 67

merge_lists(h, p)
# 15 -> 30 -> 67
