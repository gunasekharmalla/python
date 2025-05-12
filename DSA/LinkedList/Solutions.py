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


6. Solution 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def addLists(l1, l2):
    l1 = reverse(l1)
    l2 = reverse(l2)
    
    dummy = Node(0)
    temp = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10

        temp.next = Node(total % 10)
        temp = temp.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return reverse(dummy.next)

def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Input: 7 -> 2 -> 4 -> 3 (7243)
l1 = Node(7)
l1.next = Node(2)
l1.next.next = Node(4)
l1.next.next.next = Node(3)

# Input: 5 -> 6 -> 4 (564)
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

result = addLists(l1, l2)
print("Sum:")
printList(result)

Output:
Sum:
7 -> 8 -> 0 -> 7 -> None
