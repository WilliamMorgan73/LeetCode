class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums:
            arr.append(i**2)
        
        arr.sort()
        
        return arr
        
