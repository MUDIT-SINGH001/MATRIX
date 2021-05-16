m=[[10, 20, 30, 40],
                   [15, 25, 35, 45],
                   [24, 29, 37, 48],
   [32, 33, 39, 50]]
l=[]
for i in range(4):
    for j in range(4):
        l.append(m[i][j])
l.sort()
print(l[6])
    
