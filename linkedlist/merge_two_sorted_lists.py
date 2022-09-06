# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

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

def makeLinkedList(value_list):
    llist = LinkedList()
    for val in value_list:
        llist.append(val)
    return llist

values1 = [2, 4, 6, 8, 10]
values2 = [1, 2, 3, 4, 5]

llist1 = makeLinkedList(values1)
llist2 = makeLinkedList(values2)
llist1.printList()
llist2.printList()


class Solution:
    def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
        dummy = Node()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

Solution().mergeTwoLists(llist1, llist2)