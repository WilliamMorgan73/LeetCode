class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
        # Use a dictionary with count, if count > 1 do not append to result list
        # Convert string to list, combine lists, then convert to a set?

        l1 = s1.split(" ")
        l2 = s2.split(" ")

        l3 = l1 + l2
        
        result = []

        count = {}

        for word in l3:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        
        # Iterate over key-value pairs in the dictionary
        for key, value in count.items():
            if value == 1:  # Check if the value matches target_value
                result.append(key)  # Append the key to the list if there's a match
            
        return result
