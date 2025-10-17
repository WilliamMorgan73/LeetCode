class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev_val = 0
        res = 0

        for i in s[::-1]:
            val = vals.get(i)
            if val < prev_val:
                res -= val
            else:
                res += val

            prev_val = val
        
        return res

