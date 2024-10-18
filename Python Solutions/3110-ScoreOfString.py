class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxScore = 0
        
        for i in range(len(s) - 1):
            maxScore += abs(ord(s[i]) - ord(s[i+1]))
        
        return maxScore