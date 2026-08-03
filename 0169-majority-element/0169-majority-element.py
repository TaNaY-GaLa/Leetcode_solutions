class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = 0
        votes = 0
        for number in nums:
            if votes == 0:
                majority = number
            if number == majority:
                votes += 1
            else:
                votes -= 1
        return majority