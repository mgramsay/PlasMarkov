import random


def get_random_index(weights):
    rr = random.random()
    for i, w in enumerate(weights):
        rr -= w
        if rr < 0.0:
            return i
    return len(weights)-1
