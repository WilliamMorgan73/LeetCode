class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []
        #Divide list into lists of size 3
        
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] <= k:
                result.append(nums[i:i+3])
            else:
                return []

        return result
