# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def getNum(self, l):
        output_list = []


        while l:
            output_list = [l.val] + output_list
            # Increment
            l = l.next

        return output_list

    def createList(self, num):
        dummy = ListNode(0)  # dummy head
        current = dummy
        for digit in str(num)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next
        return dummy.next

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = int("".join(map(str, self.getNum(l1))))
        num2 = int("".join(map(str, self.getNum(l2))))

        # Add num1 to num2

        return (self.createList(num1 + num2))

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate total
            total = val1 + val2 + carry

            carry = total // 10

            # Add result to linkedlist
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # Return result avoiding placeholder 0
        return dummy.next