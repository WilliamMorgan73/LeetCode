class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # Convert the number to a list of digits
        numArray = list(map(int, str(num)))
        
        # Create a dictionary to store the last occurrence of each digit
        # enumerate(numArray) returns both the index (i) and the value (digit) of each item in
        # digit: i is the key-value pair in the dictionary, and i, digit in enumerate(numArray) is the iterable (the actual values)
        last_occurrence = {digit: i for i, digit in enumerate(numArray)}
        
        # Traverse the number from left to right
        for i, digit in enumerate(numArray):
            # Check if there is a larger digit in the future
            for d in range(9, digit, -1):  # Check digits larger than current one
                if last_occurrence.get(d, -1) > i:  # Larger digit found later
                    # Swap the current digit with the larger one
                    numArray[i], numArray[last_occurrence[d]] = numArray[last_occurrence[d]], numArray[i]
                    # Convert the list back to an integer and return it
                    return int("".join(map(str, numArray)))
        
        # If no swap was made, return the original number
        return num
