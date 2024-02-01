class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        totals = [0] * len(accounts)
        for i in range(0,len(accounts)):
            totals[i] = sum(accounts[i])
        return max(totals)
