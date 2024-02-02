class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        #If stack2 is empty transfer everything from stack 1 to 2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        #If stack2 is not empty, then pop top element
        if self.stack2:
            return self.stack2.pop()
        else:
            return -1
            

    def peek(self):
        """
        :rtype: int
        """
        #Same as dequeue without popping element
        #If stack2 is empty transfer from stack 1 to stack 2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2[-1]
        else:
            return -1

    def empty(self):
        """
        :rtype: bool
        """
        
        return not self.stack1 and not self.stack2
        