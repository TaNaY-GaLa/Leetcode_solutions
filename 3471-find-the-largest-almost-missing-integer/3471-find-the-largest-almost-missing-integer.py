class Solution(object):
    def largestInteger(self, nums, k):
        d = {}
        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                d[x] = d.get(x, 0) + 1
        res = -1
        for x in d:
            if d[x] == 1:
                res = max(res, x)
        return res