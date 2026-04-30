THRESHOLD = 248 * 86400 * 1000


def is_optimal(days):
    return days * 86400 * 1000 >= THRESHOLD
