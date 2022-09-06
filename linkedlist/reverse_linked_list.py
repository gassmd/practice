# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next =  new_node

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        list = []
        temp = self.head
        while(temp):
            list.append(temp.val)
            temp = temp.next
        print(list)

llist = LinkedList()

test_list = [21, 42, 3, 7, 38]

for i in test_list:
    llist.append(i)


print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()