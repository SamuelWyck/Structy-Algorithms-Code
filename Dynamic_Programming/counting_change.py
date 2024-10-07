"""Write a function, counting_change, that takes in an amount and a list of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins.

You may reuse a coin as many times as necessary.

For example,

counting_change(4, [1,2,3]) -> 4

There are four different ways to make an amount of 4:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 3
4. 2 + 2"""

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})


def _counting_change(amount, coins, i, memo):
  if (amount, i) in memo:
    return memo[(amount, i)]
  if amount == 0:
    return 1
  if i == len(coins):
    return 0

  total = 0
  coin = coins[i]
  for qty in range(0, (amount//coin) + 1):
    total += _counting_change((amount - (qty * coin)), coins, i + 1, memo)

  memo[(amount, i)] = total
  return total


counting_change(4, [1, 2, 3]) # -> 4


counting_change(8, [1, 2, 3]) # -> 10


counting_change(24, [5, 7, 3]) # -> 5


counting_change(13, [2, 6, 12, 10]) # -> 0


counting_change(512, [1, 5, 10, 25]) # -> 20119


counting_change(1000, [1, 5, 10, 25]) # -> 142511


counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # -> 1525987916
