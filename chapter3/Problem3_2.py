###큰 수의 법칙
#n : 배열의 크기 , m : 숫자가 더해지는 횟수 , k : 연속해서 더해질 수 있는 횟수
#case 1
# n,m,k=map(int,input().split())  
# number=list(map(int,input().split()))
# number.sort() 
# firstBig=number[n-1]
# secondBig=number[n-2]
# sum=0
# while(True):
#     for i in range(k):
#         sum+=firstBig
#         m=m-1
#         if(m==0):
#             print("break")
#             break
#     sum+=secondBig
#     m=m-1
#     if(m==0):
#         break
# print(sum)

#case 2 : M의 크기가 100억 이상일때 시간을 줄일 수 있다.
# n,m,k=map(int,input().split())  
# number=list(map(int,input().split()))
# number.sort() 
# firstBig=number[n-1]
# secondBig=number[n-2]
# sum=((firstBig*k)+secondBig)*(int(m/(k+1)))+(firstBig*(m%(k+1)))
# print(sum)

