for i in range(n):
    for j in range(n):
         
        # If the element is found
        if(mat[i][j] == x):
            print("Element found at (", i, ",", j, ")")
            return 1
 
print(" Element not found")
return 0
