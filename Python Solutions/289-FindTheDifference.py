from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Base case
        if s == "":
            return t

        # Create a dictonary containg counts of number in each character.

        # dict1 = Counter(s)
        # dict2 = Counter(t)

        # # Convert dict to set

        # set1 = set(dict1.items())
        # set2 = set(dict2.items())

        # # Use set difference and then return the key
        # output = dict(set2 - set1)

        # return output.popitem()[0]
    

        # Solution 2

        for char in t:
            if s.count(char) != t.count(char):
                return char