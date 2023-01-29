### 음료수 얼려 먹기
##  위,아래,좌,우 0으로 연결되어 있으면 묶는다.
##  총 몇개의 묶음이 나올까?

n,m=map(int,input().split())

# 맵 그리기
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

#DFS
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    
    if graph[x][y]==0:
        graph[x][y]=1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1

print(result)