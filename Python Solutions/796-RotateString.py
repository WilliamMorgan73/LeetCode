class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        maxSwaps = len(s)
        
        # Base case, if both strings are same
        if s == goal:
            return True
        
        # Swap the first character of the string to the end
        for i in range(maxSwaps):
            s = s[1:] + s[0]
            if s == goal:
                return True
            
        return False