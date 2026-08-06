class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for num in nums:
            output ^= num
        return output