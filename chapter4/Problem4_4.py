###게임 개발

N,M=map(int,input().split())

#지도 초기화 
d=[[0]*M for _ in range(N)]

x,y,direction=map(int,input().split())
d[x][y]=1 #현재 좌표는 방문 처리

array=[]
for i in range(N):
    array.append(list(map(int,input().split())))

#북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

count=1
turn_time=0
while(True):
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if d[nx][ny]==0 and array[nx][ny]==0:
        count+=1
        turn_time=0
        d[nx][ny]=1
        x,y=nx,ny
        continue
    else:
        turn_time+=1

    #4 방향이 모두 갈 수 없는 경우
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if(array[nx][ny]==0):
            x,y=nx,ny
        else:
            break
        turn_time=0

print(count)