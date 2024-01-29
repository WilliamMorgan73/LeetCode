class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        # Check that for each value in ransomNote can be constructed using magazine
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, '', 1)
            else:
                return False
            
        return True
