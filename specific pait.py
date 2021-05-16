mat=[[1,2,-1,4],
     [-8,-3,5,1],
     [2,0,1,4],
     [3,-1,-9,6]]
n=4
maxi=0
for a in range(0,n):
    for b in range(0,n):
        for c in range(a+1,n):
            for d in range(b+1,n):
                maxi=max(maxi,mat[c][d]-mat[a][b])
print(maxi)                
     
