import copy

def main():

    # Read input.txt
    with open('input.txt', 'r') as fp:
        lines = fp.readlines()
    lines = [ line.strip() for line in lines ]

    # Read map_size
    N, M = map(int, lines[0].split(' '))
    assert 1 <= N <= 1e3 and 1 <= M <= 1e3

    # Check the shape of given map
    assert len(lines) == N + 1
    graph = list()
    for line in lines[1:]:
        assert len(line) == M
        graph.append(list(map(int, list(line))))

    visited = copy.deepcopy(graph) 
    cnt = 0
    for x in range(N):
        for y in range(M):
            if find_icecream(x, y, visited) == True:
                cnt += 1

    print(cnt)

    return 

def find_icecream(x, y, visited):

    N = len(visited)
    M = len(visited[0])

    # out of range case
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if visited[x][y] == 0:
        visited[x][y] = 1
        find_icecream(x - 1, y, visited)
        find_icecream(x, y - 1, visited)
        find_icecream(x + 1, y, visited)
        find_icecream(x, y + 1, visited)
        return True
    else:
        return False

    return

if __name__ == '__main__':
    main()
