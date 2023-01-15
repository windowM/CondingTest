###왕실의 나이트 
pos=input();

# ord : 유니코드의 정수 값을 반환
row=ord(pos[0])-ord('a')+1
col=int(pos[1])

move=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count=0

for i in range(len(move)):
    n_row=row+move[i][0] #x
    n_col=col+move[i][1] #y
    if( n_row<1 or n_col<1 or n_row >8 or n_col>8):
        print("row:",n_row,"col:",n_col)
        continue
    count+=1
print(count)