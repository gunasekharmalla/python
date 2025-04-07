                                  ## Linked List Example Programs ##
========================================================================================================
1. What is a Node?
  => A Node is the basic building block of a linked list. Each node stores: Data
      A reference (or pointer) to the next node

Python Example: 
Basic Node Creation
=============================================
class Node:
    def __init__(self, data):
        self.data = data      # store the data
        self.next = None      # store the reference to the next node
      
Explanation:
self.data = data: stores the value of the node.
self.next = None: initially, the next pointer is set to None (no node is linked yet).

2. Creating the Head Node and Linking Manually
===============================================
# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2
node2.next = node3

       => Now the linked list looks like:
       => 10 -> 20 -> 30 -> None


3. Printing the Linked List
==============================================
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Call the function
print_list(node1)
Output:
10 -> 20 -> 30 -> None
