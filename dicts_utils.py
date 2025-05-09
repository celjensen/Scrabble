# Celeste Jensen
# 260773690

import doctest

# Counts occurrences of each character in a string and returns a dictionary
def count_occurrences(s):
    new_dict = {}
    for c in s:
        new_dict[c] = s.count(c)
    return new_dict

# Expands a dictionary into a list where keys repeat by their values
def flatten_dict(d):
    new_list = []
    for key in d:
        v = d.get(key)
        while new_list.count(key) < v:
            new_list.append(key)
    return new_list

# Computes the total score of a string based on a character-to-value dictionary
def get_word_score(s, d):
    sum_value = 0
    for c in s:
        sum_value += d.get(c, 0)
    return sum_value

# Checks if one dictionary is a subset of another
def is_subset(d, b):
    if d == {}:
        return True
    for key in d:
        if len(d) > len(b):
            return False
        if (key in b) and (d.get(key) <= b.get(key)):
            return True
        else:
            return False

# Subtracts one dictionary from another if the second is a subset of the first
def subtract_dicts(d1, d2):
    if not is_subset(d2, d1):
        return False
    for key in d2:
        if key not in d1:
            return False
    for key in d2:
        if key in d1:
            d1[key] = d1.get(key) - d2.get(key)
            if d1.get(key) <= 0:
                del d1[key]
    return True

# Creates a dictionary organizing words by length and starting letter
def create_scrabble_dict(l):
    d = {}
    for word in l:
        n = len(word)
        if n not in d:
            d[n] = [word]
        else:
            d[n].append(word)
    for key in d:
        d[key] = {}
        for word in l:
            if len(word) == key:
                if word[0] not in d[key]:
                    d[key][word[0]] = [word]
                else:
                    d[key][word[0]].append(word)
    return d

# Checks if a word is in a nested dictionary of valid words
def is_valid_word(s, d):
    if s == '':
        return False
    new_list = []
    for key in d:
        for word in d[key]:
            for c in d[key][word]:
                new_list.append(c)
    return s in new_list
