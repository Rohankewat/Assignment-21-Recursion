def printMultiples(n):      # Question no :- 9
    if n>0:
        printMultiples(n-1)
        print(2*n)
printMultiples(10)