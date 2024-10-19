class Solution(object):
    
    def invert(self, s):
        output = ""
        for character in s:
            if character == "1":
                output += "0"
            else:
                output += "1"
        return output
    
    def findnextS(self, si):
        inverted = self.invert(si)[::-1]
        nextS = si + "1" + inverted 
        return nextS
    
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s1 = "0"
        sList = [s1] 
        for i in range(2, n + 1):
            nextS = self.findnextS(sList[-1]) 
            sList.append(nextS) 

        sn = sList[-1]  
        return sn[k - 1]
