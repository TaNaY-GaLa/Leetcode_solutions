class Solution(object):
    def evaluate(self, s, knowledge):
        x = {}

        for key, value in knowledge:
            x[key] = value
        res = ""
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]
                res += x.get(key, "?")
                i = j + 1
            else:
                res += s[i]
                i += 1
        return res