class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for i in range(numRows):
            r = [1] * (i + 1)
            for j in range(1, i):
                r[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(r)
        return pascal