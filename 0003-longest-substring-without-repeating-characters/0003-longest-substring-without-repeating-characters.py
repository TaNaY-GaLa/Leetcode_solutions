class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        l = ans = 0
        for r in range(len(s)):
            if s[r] in d:
                l = max(l, d[s[r]] + 1)
            d[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans