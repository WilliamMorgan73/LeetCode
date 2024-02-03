class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        result = [0] * n

        for i in range(n):
            maxVal = 0
            #Stop out of bound error by going to whichever is larger, k or length of subarray
            for j in range(1, min(k, i + 1) + 1):
                #Get the largest value of the subarray
                maxVal = max(maxVal, arr[i - j + 1])
                #Result is the largest value j times if there are elements left
                result[i] = max(result[i], (result[i - j] if i - j >= 0 else 0) + maxVal * j)

        return result[-1]