class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        nums.sort()
        listOfLists = []
        result = []
        maxNum = 0
        minNum = 0
        #Divide list into lists of size 3
        
        for i in range(3, len(nums)+1, 3):
                listOfLists.append(nums[i-3:i])
            
        for individualList in listOfLists:
            maxNum = max(individualList)
            minNum = min(individualList)
            
            if maxNum - minNum <= k:
                result.append(individualList)
            else:
                return []
        
        return result