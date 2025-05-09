# Celeste Jensen
# 260773690

import doctest

# Creates a 2D board of specified rows and columns, filled with spaces
def create_board(int_1, int_2):
    if ((int_1 < 1) or (int_2 < 1)):
        raise ValueError('Inputs must be positive')
    final_list = []
    for i in range(int_1):
        new_list = []
        for s in range(int_2):
            new_list.append(' ')
        final_list.append(new_list)
    return final_list

# Displays a 2D board in a formatted grid
def display_board(board_list):
    print('    ', end='')
    start_col = 0
    while (start_col != (len(board_list[0]) - 1)):
        print(str(start_col) + '   ', end='')
        start_col += 1
    print(len(board_list[0]) - 1, '  ')
    start_row = 0
    while ((len(board_list)) != start_row):
        num_of_dashes = ((len(board_list[0]) * 4) - 1)
        print('  +' + '-' * int(num_of_dashes) + '+')
        print(str(start_row) + ' ', end='')
        for c in board_list[start_row]:
            print('|' + ' ' + str(c) + ' ', end='')
        print('|')
        start_row += 1
    print('  +' + '-' * int(num_of_dashes) + '+')

# Returns all elements in a given column of a 2D board
def get_vertical_axis(board_list, int_col):
    count = 0
    new_list = []
    while (count != len(board_list)):
        new_list.append(board_list[count][int_col])
        count += 1
    return new_list

# Returns the word centered at index i in a list, using consecutive non-space elements
def find_word(word_list, i):
    if (word_list[i] == ' '):
        return ''
    a = word_list[0:i]
    b = word_list[i:]
    if ' ' in a:
        space_occ = (len(a) - a[::-1].index(' '))
        first_list = a[space_occ:len(a)]
    else:
        first_list = a
    if ' ' in b:
        space_occ = (b.index(' '))
        second_list = b[0:space_occ]
    else:
        second_list = b
    new_list = first_list + second_list
    return ''.join(new_list)

# Returns the number of empty spaces from index i to the end of a list
def available_space(rc_list, i):
    return rc_list[i:].count(' ')

# Checks if a word fits starting at index i in a row or column
def fit_on_board(rc_list, letters, i):
    if rc_list[i] != ' ':
        return False
    empt_sp = available_space(rc_list, i)
    return empt_sp >= len(letters)
