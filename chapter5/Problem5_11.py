### 미로 탈출
##  (1,1)에서 (n,m)까지 최단 경로로 미로를 탈출해라!
from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

#상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위 초과일때
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            #벽일때
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

    #목표 지점 반환 = 원하는 최단 이동수
    return graph[n-1][m-1]

print(bfs(0,0))


