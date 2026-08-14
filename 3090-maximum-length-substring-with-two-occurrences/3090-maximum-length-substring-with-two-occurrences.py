class Solution(object):
    def maximumLengthSubstring(self, s):
        res = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                c = s[j]
                count[c] = count.get(c, 0) + 1
                if count[c] > 2:
                    break
                res = max(res, j - i + 1)
        return res