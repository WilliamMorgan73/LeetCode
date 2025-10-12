class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # Sum up first k elements
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum


        for i in range(k, len(nums)):
            # Shift window to right
            curr_sum = curr_sum + nums[i] - nums[i-k]

            max_sum = max(max_sum, curr_sum)

        return max_sum/float(k)