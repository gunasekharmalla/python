
#letter B 

n = 7
c = n//2 + 1
for i in range(1,n+1):
        print("* "*(c-1) +" " if i == 1 or i == n or i == c else "* "+" "*(c)+"*")


output:

* * *  
*     *
*     *
* * *  
*     *
*     *
* * *  
