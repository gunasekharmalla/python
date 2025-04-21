        Delete Node based on Position
==================================================
def deleteNode(llist, position):
    # Write your code here
    if not llist:
        return None 
    if position == 0:
        return llist.next 
    count = 0
    current = llist
    while current and count < position -1:
        current = current.next 
        count += 1
    if current is None or current.next is None:
        return llist 
    current.next = current.next.next 
    return llist
