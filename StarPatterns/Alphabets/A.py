n = 10
c = n//2 + 1
for i in range(1,n+1):
    if i == 1:
        print(" "*(n-i)+"*"*(i))
    elif i == c:
        print(" "*(n-i)+"*"*(n))
    else:
        print(" "*(n-i)+"*"+" "*((2*i)-3)+"*")

output:

         *
        * *
       *   *
      *     *
     *       *
    **********
   *           *
  *             *
 *               *
*                 *
