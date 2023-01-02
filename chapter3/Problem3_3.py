### 숫자 카드 게임
#N : 행, M : 열 개수
import time

## 내 풀이
# N,M=map(int,input().split())
# maxi=-1000;


# start_time=time.time() # 시간 측정

# for i in range(N):
#     data=list(map(int,input().split()))
#     if(maxi<min(data)):
#         maxi=min(data)
   
# end_time=time.time()

# print("time : ",(end_time-start_time))

# print(maxi)

## 책 풀이
N,M=map(int,input().split())
result=0

start_time=time.time() # 시간 측정

for i in range(N):
    data=list(map(int,input().split()))
    min_value=min(data)
    result=max(result,min_value)

end_time=time.time()

print("time : ",(end_time-start_time))

print(result)