class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set(())
        
        # Base case, empty string
        if not s:
            return 0

        max_len = 0
        i = 0

        for j in range (len(s)):
            # Shrink window until no longer seen
            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            # Increase window size
            seen.add(s[j])
            max_len = max(max_len, j-i+1)

        return max_len