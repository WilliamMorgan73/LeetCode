class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        while True:
            original = s
            
            s = s.replace('AB', '').replace('CD', '')
            
            if s == original:
                break
        
        
        return len(s)