GRID = 8

def main():
    
    with open('input.txt') as fp:
        lines = fp.readlines()

    start_point = lines[0]
    assert (len(start_point) == 2) and is_in_grid(start_point) 

    # destinations
    dsts = list()

    start_char = ord(start_point[0])
    start_num = int(start_point[1])
    for ascii_char in [start_char - 2, start_char + 2]:
        for num in [start_num - 1, start_num + 1]:
            position = chr(ascii_char) + str(num)
            if is_in_grid(position):
                dsts.append(position)
    
    for num in [start_num - 2, start_num + 2]:
        for ascii_char in [start_char - 1, start_char + 1]:
            position = chr(ascii_char) + str(num)
            if is_in_grid(position):
                dsts.append(position)
    
    print(len(dsts))

    return

def is_in_grid(position):    

    if '-' in position:
        return False

    char, num = position
    ascii_char = ord(char)
    num = int(num)

    return (97 <= ascii_char <= (97+GRID-1)) and (1 <= num <= GRID)

if __name__ == '__main__':
    main()
