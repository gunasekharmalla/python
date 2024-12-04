
def deposit():
    global balance 
    amount = float(input('enter amount to deposit')) 
    balance += amount 
    return balance 

def withdraw():
    global balance
    out_amt = float(input('enter amount to withdraw'))
    if out_amt < 0:
        print('cannot perform ')
    elif out_amt > balance:
        print('in sufficient funds') 
    else:
        balance = balance - out_amt 
    return balance 

def display():
    print( balance )

balance = 0
terminate = True 
while(terminate):
    print('1-deposit')
    print('2-withdraw') 
    print('3-display') 
    print('4-exit') 
    print('enter your choice') 
    choice = int(input()) 

    if choice == 1:
        deposit() 
    elif choice == 2:
        withdraw() 
    elif choice == 3:
        display() 
    elif choice == 4:
        terminate = False 
    else:
        print('invalid input potion ')
