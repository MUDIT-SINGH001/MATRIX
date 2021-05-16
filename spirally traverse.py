l = 0

k=0
lis=[]


while (k < m and l < n):

    # Print the first row from
    # the remaining rows
    for i in range(l, n):
        lis.append(a[k][i])

    k += 1

    # Print the last column from
    # the remaining columns
    for i in range(k, m):
        lis.append(a[i][n - 1])

    n -= 1

    # Print the last row from
    # the remaining rows
    if (k < m):

        for i in range(n - 1, (l - 1), -1):
           lis.append (a[m - 1][i])

        m -= 1

    # Print the first column from
    # the remaining columns
    if (l < n):
         for i in range(m - 1, k - 1, -1):
            lis.append (a[i][l])

         l += 1 
         
