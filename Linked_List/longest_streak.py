"""Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list."""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def longest_streak(head):
  if head is None:
    return 0
  current = head
  longest_streak = 1
  value_count = 1
  while current.next is not None:
    if current.val == current.next.val:
      value_count += 1
    else:
      if value_count > longest_streak:
        longest_streak = value_count
      value_count = 1
    current = current.next
  if value_count > longest_streak:
    longest_streak = value_count
  return longest_streak


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 5 -> 7 -> 7 -> 7 -> 6

longest_streak(a) # 3


a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 3 -> 3 -> 3 -> 3 -> 9 -> 9

longest_streak(a) # 4


a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 9 -> 9 -> 1 -> 9 -> 9 -> 9

longest_streak(a) # 3


a = Node(5)
b = Node(5)
a.next = b
# 5 -> 5

longest_streak(a) # 2


a = Node(4)
# 4

longest_streak(a) # 1


longest_streak(None) # 0




