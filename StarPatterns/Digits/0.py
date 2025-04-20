n = 5
for i in range(1,n+1):
    print(" " + "* " * (n-1) if i == 1 or i == n else("* " + "  " * (n-2) + "*"))

OutPut:
n = 5
     * * * * 
    *       *
    *       *
    *       *
     * * * * 

n = 8 

     * * * * * * * 
    *             *
    *             *
    *             *
    *             *
    *             *
    *             *
     * * * * * * * 
