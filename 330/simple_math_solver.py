from itertools import permutations
from typing import List, Union, Iterable


def find_all_solutions(
        operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    possible_operators = {"+", "-", "*"}
    if not set(operator_path).issubset(possible_operators):
        raise ValueError("Not valid operator!")

    possible_permutations = permutations(range(1, 10), 1 + len(operator_path))
    equation = "{}" + "{}".join(operator_path) + "{}"

    result = [list(permutation) for permutation in possible_permutations if
              eval(equation.format(*permutation)) == expected_result]

    if not result:
        raise ValueError("No solution for those input arguments")
    return result
