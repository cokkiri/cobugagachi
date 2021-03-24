
with open('input.txt') as fp:
    lines = fp.readlines()

N, K = list(map(int, lines[0].split(' ')))
assert (2 <= N <= 1e5) and (2 <= K <= 1e5) and (N >= K)

cnt = 0
while N > 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1
    cnt += 1

print(cnt)
