#pattern F 

n =7
c = n//2 + 1
print("* "*(n))
for I in range(2,n+1):
    print("* "*(n) if I==c else("*"))

Output:

* * * * * * * 

*

*

* * * * * * * 

*

*

*
