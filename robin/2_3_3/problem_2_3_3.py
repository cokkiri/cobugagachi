import numpy as np


with open('input_2.txt') as fp:
    lines = fp.readlines()

N, M = list(map(int, lines[0].split(' ')))
assert 1 <= N <= 1e2 and 1 <= M <= 1e2

num_table = list()
for line in lines[1:]:
    num_table.append(list(map(int, line.split(' '))))
num_table = np.array(num_table)
assert len([ x for x in num_table.flatten() if not (1 <= x <= 1e4)]) == 0

result = max([ min(x) for x in num_table ])
print(result)
