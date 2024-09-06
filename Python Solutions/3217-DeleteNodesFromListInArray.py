# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Convert the list into a set for O(1) lookup
        nums = set(nums)
        
        # Continuously update the head if its value is in nums
        while head and head.val in nums:
            head = head.next
        
        # Create a pointer to traverse the list starting from the updated head
        current = head
        
        # Loop through the rest of the list
        while current and current.next:
            # If the next node's value is in nums, skip the node
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next
                
        return head