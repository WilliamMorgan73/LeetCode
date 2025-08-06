import math

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        output = 0

        # Attempt 1: Brute force

        # Ok so the basket has a capacity

        

        # for i in range(0, len(fruits)):
        #     for j in range(0, len(baskets)):
        #         if fruits[i] <= baskets[j]:
        #             # Once we find one, we need to set basket to 0 so it cannot be used again
        #             baskets[j] = 0
        #             # Exit this loop
        #             break
                
        #         # Check if last basket
        #         elif j == (len(baskets) - 1):
        #             output += 1
        #             break
        #         else:
        #             # Check next basket
        #             next
        #     continue

        # Attempt 2: Square root decompositiion

        # Looked at explanation

        # Square root length of baskets array to get optimal partition size
        # Based on https://leetcode.com/problems/fruits-into-baskets-ii/solutions/7046650/two-solution-one-for-small-constraint-another-for-big-constraints-no-gpt-visualization-explain implementation

        # Start by defining the sectors

        sectors_mx = []
        mx = 0
        sectorSize = int(math.sqrt(len(baskets)))
        count = 1

        for i in range(len(baskets)):
            # Check if count is at sector size yet            
            if count == sectorSize:
                # Add max value of sector to array
                sectors_mx.append(mx)
                # make max the first value of next basket
                mx = baskets[i]
                # Reset count
                count = 1

            else:
                count +=1
                mx = max(mx, baskets[i]) 

        # Deal with final sector
        sectors_mx.append(mx)

        output = 0

        # Start allocation fruits

        for fruit in fruits:
            # Need index for sectors
            ind = 0

            # Need flag to know if we found the value or not, this is to update output aswell as reset max value
            flag = 1

            for j in range(0, len(baskets), sectorSize):
                if sectors_mx < fruit:
                    # Skip this segment
                    ind += 1
                    continue

                # Get the value from within this basket, smallest that fits.
                # Loop to either the end of the sector or the end of list, avoids out of bounds check 
                for y in range(j, min(j + sectorSize, len(baskets))):
                    if baskets[y] >= fruit:
                        baskets[y] = 0
                        flag = 0
                        break
                
                # If flagged
                if flag == 0:
                    sectors_mx[ind] = 0
                    # Get new max
                    for r in range(j, min(j + sectorSize, len(baskets))):
                        sectors_mx[ind] = max(baskets[r], sectors_mx[ind])
                    break
            
                ind += 1
            
            output += flag


        return output