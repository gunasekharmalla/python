# H pattern 

n= 7
c = n//2 + 1 
for I in range(1,n+1):
    print("* "+"  "*(n-2)+"*" if I!=c else("* "*(n)))

Output: 

*           *

*           *

*           *

* * * * * * * 

*           *

*           *

*           *  
