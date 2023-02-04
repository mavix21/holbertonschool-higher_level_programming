#!/usr/bin/python3
def best_score(a_dictionary):
    scores = list(a_dictionary.values())
    if len(scores) == 0:
        return None

    return max(scores)
