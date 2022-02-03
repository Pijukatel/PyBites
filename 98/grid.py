from itertools import cycle

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def _get_position_sequence_from_grid(grid: str):
    """Convert grid to sequence of positions."""
    numbers = []
    is_relevant_row = cycle([True, False])
    for row_i, row in enumerate(grid.strip().splitlines()):
        if next(is_relevant_row):
            row_numbers = row.replace("-", "").split()
            for column_i, number in enumerate(row_numbers):
                numbers.append((int(number), row_i // 2, column_i))
    return [(row, column) for (number, row, column) in sorted(numbers)]


def get_direction(old_position, new_position):
    """Get direction to next position."""
    direction_map = {(0, 1): RIGHT, (0, -1): LEFT, (1, 0): DOWN, (-1, 0): UP}
    return direction_map[new_position[0] - old_position[0], new_position[1] - old_position[1]]


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    positions = _get_position_sequence_from_grid(grid)

    output = "1 2"
    current_direction = get_direction(positions[0], positions[1])

    for number, (old_position, new_position) in enumerate(zip(positions[1:-1], positions[2:]), start=3):
        new_direction = get_direction(old_position, new_position)

        if new_direction != current_direction:
            current_direction = new_direction
            output = f"{output} {new_direction}"
            print(output)
            output = f"    {number}"
        else:
            output = f"{output} {number}"
    print(output)
