class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        prev_prev = 0
        for num in nums:
            temp = max(prev, prev_prev + num)
            prev_prev = prev
            prev = temp
        return prev