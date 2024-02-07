class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        temp = []
        result = []
        
        # Loop through each character in the string
        for char in range(len(s)):
            # Reset count
            count = 1
            
            # Check if character has already been iterated over
            if s[char] == '~':
                continue
            
            for i in range(char +1, len(s)):
                if s[i] == s[char]:
                    count += 1
                    
            # Remove that character from the string
            
            temp.append([s[char], count])
            s = s.replace(s[char], '~')
            
        # Sort temp
        
        temp.sort(key=lambda x: x[1], reverse=True)
        
        # Make result contain the correct number of each character
        
        for char, count in temp:
            result += char * count
            
        return result