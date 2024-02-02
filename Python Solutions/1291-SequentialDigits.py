class Solution(object):
    def sequentialDigits(self, low, high):
        """
        Generate sequential digits between the given range.

        :type low: int
        :type high: int
        :rtype: List[int]
        """

        result = []

        def generate_sequential(current, low, high):
            # Check if the current number is within the specified range
            if low <= current <= high:
                result.append(current)

            # Get the last digit of the current number
            lastDigit = current % 10

            # If the last digit is less than 9, generate the next sequential number
            if lastDigit < 9:
                nextNum = current * 10 + (lastDigit + 1)
                generate_sequential(nextNum, low, high)

        # Start generating sequential numbers from 1 to 9
        for i in range(1, 10):
            generate_sequential(i, low, high)

        # Return the sorted result
        return sorted(result)
