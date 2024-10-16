import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        
        # Initialize max heap, negative values are used to create a max heap (Same as in 2530)
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        output = []
        
        while max_heap:
            # Pop the character with the most remaining occurrences
            count1, char1 = heapq.heappop(max_heap)
            if len(output) >= 2 and output[-1] == output[-2] == char1:
                
                # If the last two are the same, use the next most frequent character
                if not max_heap:
                    break 
                
                count2, char2 = heapq.heappop(max_heap)
                output.append(char2)
                count2 += 1 
                
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                heapq.heappush(max_heap, (count1, char1)) # Re-insert the first character for the next iteration
                
            else:
                output.append(char1)
                count1 += 1
                
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, char1))  # Re-insert the character for the next iteration

        return ''.join(output)
