
with open('input.txt', 'r') as fp:
    lines = fp.readlines()
lines = [ line.strip() for line in lines ]

num_studnets = int(lines[0])
assert 1 <= num_studnets <= 1e5
assert len(lines[1:]) == num_studnets

student_infos = list()
for line in lines[1:]:
    name, score = line.split(' ')
    assert len(name) <= 100 and int(score) <= 100
    
    student_infos.append((name, int(score)))

sorted_infos = sorted(student_infos, key=lambda x: x[1])

for sorted_info in sorted_infos:
    print(sorted_info[0], end=' ')
