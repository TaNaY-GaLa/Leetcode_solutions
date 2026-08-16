class Solution(object):
    def countPrimes(self, n):
        p = [1] * n
        if n > 0:
            p[0] = 0
        if n > 1:
            p[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if p[i]:
                for j in range(i * i, n, i):
                    p[j] = 0
        return sum(p)