class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)

        # Loop through each temperature
        for i in range(0, len(temperatures)):
            currentTemp = temperatures[i]

            # Loop through temperatures after the current one
            for j in range(i + 1, len(temperatures)):
                if currentTemp < temperatures[j]:
                    result[i] = j - i
                    break

            # If no warmer temperature found, result[i] remains 0

        return result

    #Solution is correct but too slow for large inputs
    #Try use stack