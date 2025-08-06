class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Think I am going to do this as a two pointer problem.

        # Convert x into an array

        array = []
        for num in str(x):
            array.append (num)

        # Check if palindrome

        left = 0
        right = len(array) -1
        while left < right:
            if array[left] != array[right]:
                return False
            left +=1
            right -= 1

        return True