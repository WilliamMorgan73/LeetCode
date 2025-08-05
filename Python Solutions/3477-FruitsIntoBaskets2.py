class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """

        # Could I bruteforce
        # So go through each possble option of length 3 baskets. This will have like O(n^2) complexity.
        # Research what a segementation tree is
        # How can binary search be applied?

        # Attempt 1: Brute force

        # Ok so the basket has a capicity

        output = 0

        for i in range(0, len(fruits)):
            for j in range(0, len(baskets)):
                if fruits[i] <= baskets[j]:
                    # Once we find one, we need to set basket to 0 so it cannot be used again
                    baskets[j] = 0
                    # Exit this loop
                    break
                
                # Check if last basket
                elif j == (len(baskets) - 1):
                    output += 1
                    break
                else:
                    # Check next basket
                    next
            continue

        
        return output