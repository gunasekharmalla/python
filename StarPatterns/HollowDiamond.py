# Hollow Diamond pattern for n rows 
n=5
for I in range(1,n+1):
    print(" "*(n-I)+"*" if I==1 else(" "*(n-I)+"*"+" "*((2*I)-3)+"*"))
for I in range(n-1,0,-1):
    print(" "*(n-I)+"*" if I==1 else(" "*(n-I)+"*"+" "*((2*I)-3)+"*"))

Output:

    *

   * *

  *   *

 *     *

*       *

 *     *

  *   *

    *
