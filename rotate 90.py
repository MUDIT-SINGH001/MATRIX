l=[[1,2,3],
   [4,5,6],
   [7,8,9]]
n=3
for i in range(n):
    for j in range(n-1,-1,-1):
        print(l[j][i],end=" ")
    print()    
