###상하좌우
###L,R,U,D 를 통해 현재 위치 구하기
N=int(input())
stick=input().split()
x,y=1,1
x_value=[0,0,-1,1]
y_value=[-1,1,0,0]
data=['L','R','U','D']
for i in stick:  
    for j in range (len(data)):
        if(i==data[j]):
            nx=x+x_value[j]
            ny=y+y_value[j]
    
    if nx<1 or nx>N or ny>N or ny<1:
        continue
    x,y=nx,ny
print(x,y)