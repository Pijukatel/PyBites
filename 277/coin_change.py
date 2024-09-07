from typing import List


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """
    if n < 0 or not coins:
        return 0
    elif n == 0:
        return 1
    else:
        return make_changes(n, coins[:-1]) + make_changes(n - coins[-1], coins)
