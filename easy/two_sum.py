arr = [3, 5, -4, 8, 11, 1, -1, 6]


def two_sum(array, target):
    array.sort()
    head = 0
    tail = len(array) - 1

    while head != len(array) / 2:
        if array[head] + array[tail] == target:
            return [array[head], array[tail]]
        head += 1
    return 0
