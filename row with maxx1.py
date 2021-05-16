ma=0
f=0
for i in range(n):
    matri=arr[i].count(1)
    if(matri>ma):
        ind=i
        ma=matri
        f=1
        

if(f==0):
    return (-1)
else:
   return (ind)
