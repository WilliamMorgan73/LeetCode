class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result =[]
        tempList = []
        
        # Clone original list
        
        sortedStrs = strs[:]
        
        # Sort every string in the list alphebetically
        # Referenced from https://www.geeksforgeeks.org/python-ways-to-sort-letters-of-string-alphabetically/
        
        for i in range(0, len(sortedStrs)):
            sortedStrs[i] = ''.join(sorted(sortedStrs[i]))

        # Need to compare each element with future elements, making all the same anagrams into a new list within result
        
        for j in range(0, len(sortedStrs)):
            # Reset tempList
            tempList = []
            
            # Skip any strings that have already been sorted
            if sortedStrs[j] == '0':
                continue
            
            # Add the element into temp list
            tempList.append(strs[j])
            
            for k in range(j+1, len(sortedStrs)):
                # Find duplicates
                if sortedStrs[k] == sortedStrs[j]:
                    # Add all duplicates into temp list
                    tempList.append(strs[k])
                    
                    # Replace when found with 0
                    sortedStrs[k] = '0'
                    
            result.append(tempList)
            
        return result
        