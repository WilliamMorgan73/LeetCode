def buildLps(pattern):
    
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # We found a longer prefix-suffix match
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Fall back to the previous LPS length
                length = lps[length-1]
            else:
                # No match, stay at 0
                lps[i] = 0
                i += 1
    return lps

class Solution(object):

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # What we can do is, get the original string, push each character to the right once (wrap around) and compare to the original
        # To do this, we can concat with itself and trim the ends

        # concat = s + s

        # concat = concat[1:-1]

        # # Now we can see if s is in concat, we can do this using pythons in function

        # if s in concat:
        #     return True
        # else:
        #     return False

        
        # Now let's try KMP - With online guide

        # Surely I can build the LPS table - and then output the index of the first value greater than 1?

        lps = buildLps(s)
        lastLpsValue = lps[-1]
        n = len(s)
        
        return lastLpsValue > 0 and n % (n - lastLpsValue) == 0