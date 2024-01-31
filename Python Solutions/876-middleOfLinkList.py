Class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #Make an array based on the inputs, finding the length
        array =[]
        
        while head is not None:
            array.append(head.val)
            head = head.next

        middle = (len(array) // 2)
        
        #Return a listNode of the array from middle to end
        
        result_head = ListNode()
        current = result_head
        
        for value in array[middle:]:
            current.next = ListNode(value)
            current = current.next
        
        return result_head.next
