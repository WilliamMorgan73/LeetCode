import heapq

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Convert array into a max heap using negative values
        nums = [-num for num in nums]
        heapq.heapify(nums)  # Make sure to create the heap from the list
        
        total = 0
        
        for i in range(k):
            # Pop the smallest (which is the largest due to negative) element from the heap
            maxNum = heapq.heappop(nums)
            total += -maxNum
            
            # Push the new element into the heap
            # Use -math.ceil(-maxNum / 3) to get the correct value to push back
            heapq.heappush(nums, -((-maxNum + 2)/ 3))
            
        return total


''' Without heap
class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Create a copy of nums to avoid mutating the original input list
        nums_copy = nums[:]
        
        i = 1
        total = 0
        while i <= k:
            maxNum = max(nums_copy)
            total += maxNum
            maxIdx = nums_copy.index(maxNum)
            nums_copy[maxIdx] = ((maxNum + 2)/3)
            
            i += 1
            
        return total

'''