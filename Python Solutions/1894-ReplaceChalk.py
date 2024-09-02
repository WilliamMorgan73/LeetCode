class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        total = sum(chalk)

        # Check if the total is less than k
        k = k % total
        
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
            
            # Check if the index is out of bounds
            if i == len(chalk):
                i = 0
                
        return i