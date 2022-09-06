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

        # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

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

    # Utility function to print the linked LinkedList
    def printList(self):
        list = []
        temp = self.head
        while(temp):
            list.append(temp.val)
            temp = temp.next
        print(list)

    def hasCycle(self, head: Node) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next      #iterates fast and slow pointers with fast going x2 faster
            if fast == slow:
                return True
            return False

def make_list(elements):
    head = Node(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(element)
    return head

llist = LinkedList()

list_elements = [21, 42, 3, 7, 38]

test_list = make_list(list_elements)

for i in test_list:
    print(i.val)

test_cycle = llist.hasCycle(llist.head)
print(test_cycle)
