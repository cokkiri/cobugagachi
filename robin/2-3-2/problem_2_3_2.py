DEBUG = False
# DEBUG = True

with open('./input.txt') as fp:
    lines = fp.readlines()

N, M, K = map(int, lines[0].split(' '))
assert (2 <= N <= 1e3) and (1 <= M <= 1e4) and (1 <= K <= 1e5) and (K <= M), 'N, M, K = {}, {}, {}'.format(N, M, K)

nums = map(int, lines[1].split(' '))
sorted_nums = sorted(nums, reverse=True)
assert len(sorted_nums) == N, 'len = {}, N = {}'.format(len(sorted_nums), N)

cnt = 0
sum = 0
brk_flag = False
num1, num2 = sorted_nums[:2]

while not brk_flag:
    for idx in range(K):
        sum += num1
        cnt += 1
        if DEBUG:
            print(num1, sum)
        if cnt == M:
            brk_flag = True
    sum += num2
    cnt += 1
    if DEBUG:
        print(num2, sum)
    if cnt == M:
        brk_flag = True

print(sum)
