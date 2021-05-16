arr= [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 1],
      ]
ma=0
f=0
for i in range(3):
    m=arr[i].count(1)
    if(m>ma):
        ind=i
        ma=m
        f=1
        

if(f==0):
    print(-1)
else:
    print(i)
