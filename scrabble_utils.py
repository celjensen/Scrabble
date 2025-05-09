# Celeste Jensen
# 260773690

import dicts_utils
import board_utils
import random
import doctest

# Displays the rack of a player
def display_rack(d):
    l = dicts_utils.flatten_dict(d)
    for s in l:
        print(s.upper(), end=' ')

# Checks if a rack contains all letters in a string and updates it if so
def has_letters(d, s):
    s_dict = dicts_utils.count_occurrences(s)
    return dicts_utils.subtract_dicts(d, s_dict)

# Refills a rack from the pool until it has n letters or the pool is empty
def refill_rack(r, p, n):
    p_2 = dicts_utils.flatten_dict(p)
    r_2 = dicts_utils.flatten_dict(r)
    while ((len(r_2) < n) and (len(p_2) > 0)):
        choice = random.choice(p_2)
        p_2.remove(choice)
        r_2.append(choice)
    new_p = {}
    for c in p_2:
        new_p[c] = p_2.count(c)
    new_r = {}
    for c in r_2:
        new_r[c] = r_2.count(c)
    p.clear()
    p.update(new_p)
    r.clear()
    r.update(new_r)

# Computes the score of a list of words if all are valid
def compute_score(l, d1, d2):
    score = 0
    for s in l:
        if not dicts_utils.is_valid_word(s, d2):
            return 0
        score += dicts_utils.get_word_score(s, d1)
    return score

# Places tiles on the board and returns the list of words formed
def place_tiles(b, s_play, row, col, s_dir):
    if s_dir == 'right':
        i = 0
        i_2 = 0
        while i_2 < len(s_play):
            if b[row][col + i] == ' ':
                b[row][col + i] = s_play[i_2]
                i += 1
                i_2 += 1
            else:
                i += 1
        word_list = []
        w = board_utils.find_word(b[row], col)
        word_list.append(w)
        place = b[row]
        for i in range(len(place[col:len(s_play) + 1])):
            v = board_utils.get_vertical_axis(b, i)
            w_2 = board_utils.find_word(v, col)
            if place[i] not in s_play:
                continue
            if (len(w_2) > 1):
                word_list.append(w_2)
    elif s_dir == 'down':
        l = board_utils.get_vertical_axis(b, col)
        for i in range(len(s_play)):
            l[row + i] = s_play[i]
        s = ''.join(l[row:])
        i = 0
        i_2 = 0
        while i_2 < (len(s)):
            if b[row + i][col] == ' ':
                b[row + i][col] = s[i_2]
                i += 1
                i_2 += 1
            else:
                i += 1
        word_list = []
        w = board_utils.find_word(l, col)
        word_list.append(w)
        for i in range(len(l[row:len(s_play) + 1])):
            w_2 = board_utils.find_word(b[i], row)
            if l[i] not in s_play:
                continue
            if (len(w_2) > 1):
                word_list.append(w_2)
    else:
        word_list = []
    return word_list

# Makes a move on the board after validating fit and rack contents
def make_a_move(b, r, s_play, row, col, s_dir):
    if not ((s_dir == 'right') or (s_dir == 'down')):
        return []
    if s_dir == 'right':
        if not board_utils.fit_on_board(b[row], s_play, col):
            raise IndexError('Not enough space on the board.')
        if not has_letters(r, s_play):
            raise ValueError('Letters not on your rack.')
        play_dict = dicts_utils.count_occurrences(s_play)
        dicts_utils.subtract_dicts(r, play_dict)
    else:
        l = board_utils.get_vertical_axis(b, col)
        if not board_utils.fit_on_board(l, s_play, row):
            raise IndexError('Not enough space on board.')
        if not has_letters(r, s_play):
            raise ValueError('Letters not on your rack.')
        play_dict = dicts_utils.count_occurrences(s_play)
        dicts_utils.subtract_dicts(r, play_dict)
    return place_tiles(b, s_play, row, col, s_dir)
