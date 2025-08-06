class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # count = 0
        # j = 0
        # prevIndex = 0
        # i = 0

        # while i <  len(haystack):
        #     if haystack[i] == needle[j]:
        #         # Check if start of word, if so remember the index of the next character for backtracking
        #         if j == 0:
        #             prevIndex = i+1
                
        #         if count == (len(needle)-1):
        #             return (i - count)
                
        #         # Increment count
        #         count += 1

        #         # Increment pointers
        #         i += 1
        #         j +=1
                
        #     else:

        #         # Check if count > 0
        #         if count > 0:
        #             # Roll back
        #             i = prevIndex
        #         else:
        #             # Next char
        #             i +=1

        #         # Increment pointer, reset count
        #         j=0
        #         count = 0

        # return -1    

        # Slicing attempt

        i = 0
        j = 0

        m = len(needle)

        for i in range(len(haystack)):
            if haystack[i:i+m] == needle:
                return i
            
        
        return -1
