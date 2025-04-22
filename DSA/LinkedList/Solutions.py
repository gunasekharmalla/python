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
====================================
problem : Finding Intersection of two Lists 
List 1: 10 -> 20 -> 30 -> 40 -> 50
List 2:      15 -> 30 -> 40 -> 50

def get_intersection(head1, head2):
    if not head1 or not head2:
        return None
    
    a, b = head1, head2
    
    while a != b:
        a = a.next if a else head2
        b = b.next if b else head1
        
    if a:
        print(f"✅ Intersection point at node with value: {a.data}")
    else:
        print("❌ No intersection found")
    return a

Output: 
✅ Intersection point at node with value: 30
