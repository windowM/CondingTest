###시각 : 3이 하나라도 포함되는 경우의 수를 구해라
N=int(input())
count=0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)




