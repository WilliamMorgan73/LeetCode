class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        
        while t > 0:
            # Increase num by 2 (same as decreasing final result by 1)
            num += 2
            t-=1
            
        return num