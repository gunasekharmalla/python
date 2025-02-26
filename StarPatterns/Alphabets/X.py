
n = 5

for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(i) if i==1 else " "*(n-i)+"*"+" "*((2*i)-3)+"*")
for i in range(2,n+1):
    print(" "*(n-i)+"*"*(i) if i==1 else " "*(n-i)+"*"+" "*((2*i)-3)+"*")

output:

*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
