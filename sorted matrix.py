from numpy import *
temp=[]
l=[]
l1=[]
M=[[1,5,3],[2,8,7],[4,6,9]]
for i in range(3):
    for j in range(3):
        temp.append(M[i][j])
temp.sort()
return (np.array(temp).reshape(N,N))    
