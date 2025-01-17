"""Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
  current1 = head_1.next
  current2 = head_2
  count = 0
  tail = head_1
  while current1 is not None and current2 is not None:
    if count % 2 != 0:
      tail.next = current1
      tail = tail.next
      current1 = current1.next
      count += 1
    elif count % 2 == 0 or count == 0:
      tail.next = current2
      tail = tail.next
      current2 = current2.next
      count += 1
  if current2 == None:
    tail.next = current1
  elif current1 == None:
    tail.next = current2
  
  return head_1


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z


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

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z -> d -> e -> f


s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

zipper_lists(s, one)
# s -> 1 -> t -> 2 -> 3 -> 4


w = Node("w")
# w

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 

zipper_lists(w, one)
# w -> 1 -> 2 -> 3


one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 

w = Node("w")
# w

zipper_lists(one, w)
# 1 -> w -> 2 -> 3

