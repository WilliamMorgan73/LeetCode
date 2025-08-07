from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # dict1 = Counter(s)
        # dict2 = Counter(t)

        # return dict1 == dict2
        
        # But this is not really the point, so let's try something else

        # Basecase, different lengths

        if len(s) != len(t):
            return False

        # Iterate through each character in the string, creating a dict

        counter = {}

        for char in s:
            counter[char] = counter.get(char,0) + 1

        # Check if all letters in t
        
        for char in t:
            # Check if letter exits/any more occurences of it left
            if char not in counter or counter[char] == 0:
                return False
            
            # Decrease count
            counter[char] -= 1

        return True