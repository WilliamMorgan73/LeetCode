class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Create a sorted array, so that we can get the rank of each element
        tempArray = sorted(arr)
        
        # Create a dictionary to store the rank of each element
        rankDict = {}
        rank = 1
        for i in range(len(tempArray)):
            if tempArray[i] not in rankDict:
                rankDict[tempArray[i]] = rank
                rank += 1
                
        # Create a list to store the rank of each element
        result = []
        
        # Get the rank of each element from the dictionary
        for i in range(len(arr)):
            result.append(rankDict[arr[i]])
            
        return result