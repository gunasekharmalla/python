def add():
    print('enter a,b values') 
    a , b = map(int,input().split()) 
    print(a+b) 

def sub():
    print('enter a,b values') 
    a,b = map(int,input().split()) 
    diff = a-b 
    print(diff) 

def mul():
    print('enter a,b values') 
    a , b = map(int,input().split()) 
    prod = a*b 
    print(prod) 

def div():
    print('enter a,b values') 
    a , b = map(int,input().split()) 
    try:
        quo = a/b 
        print(quo) 
    except ZeroDivisionError:
        print('cannot perform zero division ')
    

def mod():
    print('enter a,b values') 
    a , b = map(int,input().split()) 
    try:
        rem = a%b 
        print(rem)
    except ZeroDivisionError:
        print('cannot perform zero division') 

run = True 
while(run):
    print('1-addition') 
    print('2-subtraction') 
    print('3-multiplication') 
    print('4-division') 
    print('5-modulus')
    print('6-exit') 

    print('enter your choice') 
    choice = int(input()) 

    if choice == 1:
        add() 
    elif choice == 2:
        sub() 
    elif choice == 3:
        mul()
    elif choice ==4:
        div() 
    elif choice == 5:
        mod() 
    elif choice == 6:
        run = False 
    else:
        print('invalid input option ')