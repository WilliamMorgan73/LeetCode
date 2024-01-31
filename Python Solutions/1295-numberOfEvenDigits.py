class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        listOfDigits = []

        for i in nums:
            #Turn integer into list
            listOfDigits = [int(x) for x in str(i)]
            
            if len(listOfDigits) % 2 ==0:
                count += 1
            else:
                continue
            
        return count