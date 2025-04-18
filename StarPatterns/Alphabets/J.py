n = 10
m = n // 2 + 1
for i in range(n,0,-1):
    if i ==1:
        print(" " * (n-1) + " *")
    elif i <= m:
        print(" " * (n-i-1) + " *" + " " * (i-1) + "*")
    elif i == n:
        print(" *" * n)
    else:
        print(" " *(n-1) + " *")

Output:

n =10

* * * * * * * * * *
          *
          *
          *
    *     *
     *    *
      *   *
       *  *
        * *
          *

n = 5

 * * * * *
     *
  *  *
   * *
     *
        
        
