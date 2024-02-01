class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Base case if length = 2
        
        if len(nums) == 2:
            nums[1] = sum(nums[2:1:-1])
            return nums
        
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
    
