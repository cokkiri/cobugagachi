
with open('input.txt') as fp:
    lines = fp.readlines()

start_point = lines[0]
row = int(start_point[1])
col = int(ord(start_point[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

cnt = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        cnt += 1

print(cnt)
