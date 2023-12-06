#!/usr/bin/python3
def best_score(a_dictionary):
    """
    best_score - get key of best score in dictionary
    @a_dictionary: the dictionary
    Return: the best score
    """
    score = None
    if a_dictionary:
        for key in a_dictionary.keys():
            if not score:
                score = key
            if a_dictionary[score] < a_dictionary[key]:
                score = key

    return score
