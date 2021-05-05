
with open('input.txt', 'r') as fp:
    lines = fp.readlines()
lines = [ line.strip() for line in lines ]

N, K = list(map(int, lines[0].split(' ')))
assert 1 <= N <= 1e5 and 0 <= K <= N

list_a = list(map(int, lines[1].split(' ')))
list_b = list(map(int, lines[2].split(' ')))

list_a.sort()
list_b.sort(reverse=True)

for i in range(K):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else:
        break

print(sum(list_a))
