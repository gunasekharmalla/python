# diamond pattern 

n=5
for I in range(1,n+1):
    print(" "*(n-I)+"*" if I==1 else(" "*(n-I)+"*"*((2*I)-1)))
for I in range(n-1,0,-1):
    print(" "*(n-I)+"*" if I==1 else(" "*(n-I)+"*"*((2*I)-1)))

Output:


    *

   ***

  *****

 *******

*********

 *******

  *****

   ***

    *

