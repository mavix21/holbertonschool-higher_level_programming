#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    score_sum = 0
    weight_sum = 0
    for item in my_list:
        if not isinstance(item, tuple) or len(item) != 2:
            raise TypeError("Elements in my_list must be tuples of length 2")
        score, weight = item
        score_sum += score * weight
        weight_sum += weight

    return score_sum / weight_sum
