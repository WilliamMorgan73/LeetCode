class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        outputString = ""
        count = 0
        
        for i in range(len(s)):
            # If the current character is the same as the next 2 characters
            if i < len(s) - 2 and s[i] == s[i + 1] == s[i + 2]:
                continue
            else:
                outputString += s[i]
                
        return outputString
            
        
        