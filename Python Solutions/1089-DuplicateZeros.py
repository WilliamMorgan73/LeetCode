class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        # Loop through each element
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                # Maintain original length
                arr.pop()
                # Increment i to skip duplicate zero
                i += 2
            else:
                i += 1
            