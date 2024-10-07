"""Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains a cycle."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_cycle1(head):
  current = head
  visited = set()
  while current is not None:
    if current in visited:
      return True
    visited.add(current)
    current = current.next
  return False


def linked_list_cycle(head):
  slow = head
  fast = head
  first_cycle = True
  while fast is not None and fast.next is not None:
    if not first_cycle and fast is slow:
      return True
    elif first_cycle:
      first_cycle = False
    fast = fast.next.next
    slow = slow.next
  return False


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.next = b
b.next = c
c.next = d
d.next = b # cycle
#         _______
#       /        \
# a -> b -> c -> d 

linked_list_cycle(a)  # True


q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
q.next = r
r.next = s
s.next = t
t.next = u
u.next = q # cycle
#    ________________
#  /                 \
# q -> r -> s -> t -> u 

linked_list_cycle(q)  # True


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d 

linked_list_cycle(a)  # False


q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
q.next = r
r.next = s
s.next = t
t.next = u
u.next = t # cycle
#                   __
#                 /   \
# q -> r -> s -> t -> u 

linked_list_cycle(q)  # True


p = Node('p')
# p

linked_list_cycle(p) # False


linked_list_cycle(None) # False
