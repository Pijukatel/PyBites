from collections import Counter


def combine_and_count(a: dict[str, int], b: dict[str, int]) -> dict:
    if not (isinstance(a, dict) and isinstance(a, dict)):
        raise TypeError  # This should be checked by mypy, not unit tests!!!
    return dict(Counter(a) + Counter(b))
