a=[[5,2,6,4],
   [1,4,5,6],
   [7,5,3,6],
   [4,5,6,7]]
f=0
for i in range(4):
    for j in range(4):
        if(a[0][i] in a[j]):
            f=1
        else:
            f=0
            break
    if(f==1):
        print(a[0][i])
    
