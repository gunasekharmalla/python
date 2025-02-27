
n = 7
for i in range(1,n+1):
    print("*"*(n)if i==1 else (" "*(1)+"*"*(n)if i==n else " "*((n-i)+1)+"*"))

output:

*******
      *
     *
    *
   *
  *
 *******
