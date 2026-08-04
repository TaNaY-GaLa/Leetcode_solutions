class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mini = min(nums)
        maxi = max(nums)
        visited = set(nums)
        miss = []
        for num in range(mini, maxi + 1):
            if num not in visited:
                miss.append(num)
        return miss