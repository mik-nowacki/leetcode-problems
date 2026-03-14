class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr1 = max1 = 0
        spare1 = k

        i = j = 0

        while i < len(nums):
            if nums[i] == 1: # right end forward
                curr1 += 1
                i += 1
            elif nums[i] == 0 and spare1 > 0: # right end forward - use k
                curr1 += 1
                spare1 -= 1
                i += 1
            elif spare1 == 0: # left end forward
                if nums[j] == 0: # free up k
                    spare1 += 1
                curr1 -= 1
                j += 1
            if curr1 > max1:
                max1 = curr1
                
        return max1
        
# 1hr 36m 56s