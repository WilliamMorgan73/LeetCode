# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        # If n is even, there are no solutions possible
        if n % 2 == 0:
            return []
        
        # If n is 1, only the root
        if n == 1:
            return [TreeNode(0)]

        result = []
        
        # Iterate over odd numbers from 1 to n (inclusive) with a step of 2
        for i in range(1, n, 2):
            # Recursively generate all possible left subtrees with i nodes
            leftSubtrees = self.allPossibleFBT(i)
            # Recursively generate all possible right subtrees with n - 1 - i nodes
            rightSubtrees = self.allPossibleFBT(n - 1 - i)
            
            # Iterate over all combinations of left and right subtrees
            for left in leftSubtrees:
                for right in rightSubtrees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    # Create a root node for each combination and add it to the result
                    result.append(root)

        return result
