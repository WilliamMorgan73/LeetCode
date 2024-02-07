class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Merge nums2 into nums1
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        
        # Sort only the first m + n elements of nums1
        nums1[:m + n] = sorted(nums1[:m + n])
