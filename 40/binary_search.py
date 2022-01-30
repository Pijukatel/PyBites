def binary_search(sequence, target):
    if target < sequence[0] or target > sequence[-1]:
        return

    start = 0
    end = len(sequence) - 1
    while start <= end:
        middle = (start + end) // 2
        if target < sequence[middle]:
            end = middle - 1
        elif target > sequence[middle]:
            start = middle + 1
        elif sequence[middle] == target:
            return middle
    return
