class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)

        # Skipping last index as always going to output 0, then going down until -1 (index 0)
        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            # Ensuring we do not get an bound error
            while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                if result[j] > 0:
                    j = j + result[j]
                else:
                    # Break the loop if no warmer temperature is found
                    j = len(temperatures)  
            if j < len(temperatures):
                result[i] = j - i

        return result
