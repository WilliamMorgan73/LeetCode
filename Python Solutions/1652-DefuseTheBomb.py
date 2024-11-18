class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # Base case, if k = 0
        
        originalK = k
        
        if k == 0:
            # Outputput a list full of 0 of len code
            return [0] * len(code)
        
        # If k is negative
        if k < 0:
            # Reverse the list
            code = code[::-1]
            # Make k positive
            k = -k
            
        # Initialize the outputput list
        output = []
        
        # Iterate over the code list
        
        for i in range(len(code)):
            # Initialize the sum
            s = 0
            # Iterate over the next k elements
            for j in range(1, k + 1):
                # Add the jth element to the sum
                s += code[(i + j) % len(code)]
            # Append the sum to the outputput list
            output.append(s)
            
        if originalK < 0:
            # Reverse the list back
            output = output[::-1]
            
        return output