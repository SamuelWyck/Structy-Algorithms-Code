"""Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative."""

def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})


def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  if amount < 0:
    return False
  if amount == 0:
    return True
  if not numbers:
    return False

  for number in numbers:
    memo[amount] = _sum_possible(amount - number, numbers, memo)
    if memo[amount]:
      return True

  return False


sum_possible(8, [5, 12, 4]) # -> True, 4 + 4


sum_possible(15, [6, 2, 10, 19]) # -> False


sum_possible(13, [6, 2, 1]) # -> True


sum_possible(103, [6, 20, 1]) # -> True


sum_possible(12, []) # -> False


sum_possible(12, [12]) # -> True


sum_possible(0, []) # -> True


sum_possible(271, [10, 8, 265, 24]) # -> False


sum_possible(2017, [4, 2, 10]) # -> False


sum_possible(13, [3, 5]) # -> true


sum_possible(10, [4, 5, 7]) # -> true
