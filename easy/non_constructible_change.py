arr = [5, 7, 1, 1, 2, 3, 22]


def nonConstructibleChange(cents):
    cents.sort()
    changes = 0

    for cent in cents:
        if cent > changes + 1:
            return changes + 1
        changes += cent

    return changes + 1
