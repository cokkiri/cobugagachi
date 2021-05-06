
with open('input.txt', 'r') as fp:
    lines = fp.readlines()
lines = [ line.strip() for line in lines ]

num, length = list(map(int, lines[0].split(' ')))
assert 1 <= num <= 1e6 and 1 <= length <= 2e9

lengths = list(map(int, lines[1].split(' ')))
assert len([x for x in lengths if x < length]) == 0
assert len([x for x in lengths if type(x) != type(1) or not (0 <= x <= 1e10)]) == 0

start = 0
end = max(lengths)

result = 0
while(start <= end):
    sum = 0
    mid = (start + end) // 2
    for x in lengths:
        if x > mid:
            sum += x - mid
    if sum < length:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
