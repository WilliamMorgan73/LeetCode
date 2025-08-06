class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        # First approach

        # output = ""

        # while word1 != "" and word2 != "":
        #     # Add first character of strings to output
        #     output += word1[0]
        #     output += word2[0]

        #     # Use slicing to remove first character

        #     word1 = word1[1:]
        #     word2 = word2[1:]

        # # Append both strings to end, since one should be empty

        # output += word1
        # output += word2



        # Let's try a two pointer approach

        m = len(word1)
        n = len(word2)

        output = ""

        i = 0
        j = 0

        while i < m or j < n:
            if i < m:
                output += word1[i]
                i+=1
            if j < n:
                output += word2[j]
                j+=1

        return output