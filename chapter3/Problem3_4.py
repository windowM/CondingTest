### 1이 될때까지 
### 어떤 수 N을  [ 1.1을 뺀다. 2.K로 나눈다. ] 
### 두가지 방법만으로 1이 되는 최소 횟수를 구해라

N,K=map(int,input().split())
cnt=0;
while N>=K:
    while N%K!=0:
        N=N-1
        cnt+=1
    N=N/K
    cnt+=1
while N>1:
    N-=1
    cnt+=1

print(cnt)