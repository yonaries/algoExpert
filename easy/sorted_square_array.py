arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sort_square(array):
    new_arr = []
    for value in array:
        new_arr.append(value * value)
    return new_arr
