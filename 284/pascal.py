from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N == 0:
        return []
    row = [1]
    for i in range(N - 1):
        padded_row = row + [0]
        row = [x + y for x, y in zip(padded_row, reversed(padded_row))]
    return row
