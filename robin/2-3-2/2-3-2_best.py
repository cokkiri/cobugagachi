

with open('./input.txt') as fp:
    lines = fp.readlines()

N, M, K = map(int, lines[0].split(' '))
assert 2<=N<=1e3 and 1<=M<=1e4 and 1<=K<=1e5
assert K<=M

nums = map(int, lines[1].split(' '))
nums.sort(reverse=True)
assert len(nums)==N

num1, num2 = nums[:2]

# cnt: # of num1
cnt = (M // (K+1)) * K
cnt += M % (K+1)

sum = cnt * num1
sum += (M-cnt) * num2

print(sum)

