def printRev(n):         # Question no :- 10
    if n>0:
        r = n%10
        n = n//10
        print(r,end=" ")
        printRev(n)
printRev(135)