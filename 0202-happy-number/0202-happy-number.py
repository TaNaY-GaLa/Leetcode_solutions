class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum
        return False