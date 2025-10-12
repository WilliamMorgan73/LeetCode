class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        sum = 0
        min_len = len(nums)+ 1

        for right in range(len(nums)):
            # Expand window
            sum += nums[right]

            # Shrink window as long as valid
            while sum >= target:
                min_len = min(min_len, right-left+1)
                sum -= nums[left]
                left += 1

        return 0 if min_len == len(nums)+ 1 else min_len