arr1 = [5, 1, 22, 25, 6, -1, 8, 10]
arr2 = [1, 6, -1, 10]


def validate_subsequence(origin, sub):
    index = 0
    for value in origin:
        if index == len(sub):
            break
        if sub[index] == value:
            index += 1

    return index == len(sub)
