#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    weight_sum = 0
    sum_of_weights = 0
    for t in my_list:
        a, b = t
        weight_sum += a * b
        sum_of_weights += b

    return weight_sum / sum_of_weights
