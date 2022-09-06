class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head

class Solution(object):

    def isPalindrome(self, head):               # two ptr solution (Fast/slow) uses no extra memory
        fast, slow = head, head                 # starting where slow pointer ends (midpoint of list), reverse second half of list
        rev = None                              # check if both halves are equal
        flag = 1
        if not head:
            return True
        while fast and fast.next:               #fast ptr iterates through whole list until null
            if not fast.next.next:
                flag = 0
                break
            fast = fast.next.next               # iterates fast pointer
            temp = slow
            slow = slow.next                    # slow pointer will hit midpoint when null hit
            temp.next = rev
            rev = temp
        #print(fast.val)
        fast = slow.next
        slow.next = rev
        if flag:
            slow = slow.next
        while fast and slow:
            if fast.data != slow.data:
                return False
            fast = fast.next
            slow = slow.next
        return True

    def isPalindrome1(self, head:ListNode) -> bool:         # decently fast solution but uses a small amount of extra memory
        nums = []

        while head:
            nums.append(head.data)
            head = head.next

        l, r = 0 , len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def isPalindrome3(self, head: ListNode) -> bool:
        vals = []
        currentNode = head

        while currentNode is not None:
            vals.append(currentNode.val)
            currentNode = currentNode.next
        return vals == vals[::-1]

    def isPalindrome4(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node = head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

    def isPalindrome5(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


head = make_list([1,2,3,2,1])
ob1 = Solution()
print(ob1.isPalindrome1(head))