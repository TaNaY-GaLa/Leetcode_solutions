class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)): 
            left = max(nums[:i + 1]) 
            right = min(nums[i:]) 
            if left - right <= k: 
                return i 
        return -1