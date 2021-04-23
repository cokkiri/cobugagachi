from collections import deque

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]


with open('input.txt') as fp:
    lines = fp.readlines()
lines = [ line.strip() for line in lines ]

N, M = map(int, lines[0].split(' '))
assert 4 <= N <= 200 and 4 <= M <= 200

graph = [ list(map(int, list(line))) for line in lines[1:] ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))