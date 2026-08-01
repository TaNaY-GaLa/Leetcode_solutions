class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def choose(i, j):
            if i == j:
                return nums[i]
            l = nums[i] - choose(i + 1, j)
            r = nums[j] - choose(i, j - 1)
            return max(l,r)
        return choose(0, len(nums) - 1) >= 0