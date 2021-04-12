import numpy as np

from game_character import GameCharacter

DEBUG = True
# DEBUG = False

def check_pos(character, given_map):

    fwd_pos_x = character.fwd_pos_x
    fwd_pos_y = character.fwd_pos_y

    width = given_map.shape[1]
    height = given_map.shape[0]

    # beyond map
    if fwd_pos_x < 0 or fwd_pos_x >= height or fwd_pos_y < 0 or fwd_pos_y >= width:
        if DEBUG:
            print('INFO-DEBUG:: beyond map!!!')
        flag = False
    # is_sea
    elif given_map[fwd_pos_x][fwd_pos_y] == 1:
        if DEBUG:
            print('INFO-DEBUG:: fwd_pos is in the sea!!!')
        flag = False
    # visited
    elif (fwd_pos_x, fwd_pos_y) in character.visited:
        if DEBUG:
            print('INFO-DEBUG:: already visited!!!')
        flag = False
    else:
        flag = True

    return flag

def is_in_the_sea(position, given_map):

    bwd_pos_x = position[0]
    bwd_pos_y = position[1]

    if given_map[bwd_pos_x][bwd_pos_y] == 1:
        flag = True
    else:
        flag = False

    return flag

with open('input.txt') as fp:
    lines = fp.readlines()
    lines = [ line.strip() for line in lines ]

N, M = map(int, lines[0].split(' '))
assert (3 <= N <= 50) and (3 <= M <= 50)

pos_x, pos_y, direction = map(int, lines[1].split(' '))
assert (1 <= pos_x <= N) and (1 <= pos_y <= M) and (direction in [0, 1, 2, 3])

character = GameCharacter(pos_x, pos_y, direction)

given_map = list()
for line in lines[2:]:
    row = map(int, line.split(' '))
    assert len(row) == M
    given_map.append(row)
assert len(given_map) == N

given_map = np.array(given_map)
assert given_map[pos_x][pos_y] == 0

if DEBUG:
    print('INFO-DEBUG:: curr_pos: x={}, y={}'.format(pos_x, pos_y))

cnt = 0
while True:
    character.get_left_position()
    if DEBUG:
        print('INFO-DEBUG:: curr_pos: x={}, y={}'.format(character.pos_x, character.pos_y))
        print('INFO-DEBUG:: left_pos: x={}, y={}'.format(character.fwd_pos_x, character.fwd_pos_y))

    flag = check_pos(character, given_map)
    character.turn_left()
    if DEBUG:
        print('INFO-DEBUG:: turn_left: direc={}'.format(character.direction))
        print('\n')

    if flag:
        character.go_forward()
        if DEBUG:
            print('INFO-DEBUG:: curr_pos: x={}, y={}'.format(character.pos_x, character.pos_y))
        character.save_memory((character.pos_x, character.pos_y))
        if DEBUG:
            print('INFO-DEBUG:: memory: {}'.format(character.visited))
        cnt = 0
    else:
        character.init_fwd_pos()
        cnt += 1

    if cnt == 4:
        character.get_backward_position()
        if is_in_the_sea((character.bwd_pos_x, character.bwd_pos_y), given_map):
            break
        else:
            character.go_backward()
            cnt = 0

    if DEBUG:
        print('-----------------------------------')

print(character.visited, len(character.visited))