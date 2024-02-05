class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        for i in range(len(s)):
            currentCharacter = s[i]
            isUnique = True
            
            if currentCharacter == '0':
                continue
            
            # Check if character appears elsewhere in the string
            for j in range(i+1,len(s)):
                if s[j] == currentCharacter:
                    isUnique = False
                    s = s.replace(s[j], '0')
                    break
                
            # Return the index (i) of the first unique character
            if isUnique:
                return i
            else:
                continue
            
        # If no unique character found, return -1
        return -1
        