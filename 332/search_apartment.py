from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    if direction not in [EAST,WEST]:
        raise ValueError

    if direction == EAST:
        buildings = list(reversed(buildings))

    number_of_buildings = len(buildings)
    buildings_with_view = [0]
    for i in range(1, number_of_buildings):
        if buildings[i] > buildings[buildings_with_view[-1]]:
            buildings_with_view.append(i)

    if direction == EAST:
        buildings_with_view = list(
            reversed([number_of_buildings - building_index - 1 for building_index in buildings_with_view]))

    return buildings_with_view
