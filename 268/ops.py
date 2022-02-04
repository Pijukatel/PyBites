from typing import NamedTuple, Deque
from collections import deque


class Node(NamedTuple):
    number: int
    n: int


def num_ops(number):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """

    def _get_new_nodes(old_node):
        value, n = old_node
        return [Node(value * 2, n + 1), Node(value // 3, n + 1)]

    explored_nodes = {1: 0}
    unexplored_nodes: Deque[Node] = deque([Node(2, 1), Node(0, 1)])

    while True:
        current_node = unexplored_nodes.pop()
        if current_node.number == number:
            return current_node.n
        elif current_node.number in explored_nodes:
            continue
        else:
            explored_nodes.update([current_node])
            unexplored_nodes.extendleft(_get_new_nodes(current_node))
