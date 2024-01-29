class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        #Base case
        if num == 0:
            return 0
        elif num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2)
        else:
            return 1 + self.numberOfSteps(num - 1)