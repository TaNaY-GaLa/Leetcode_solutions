class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sold = 0
        for p in prices[1:]:
            if p < buy:
                buy = p
            else:
                sold = max(sold, p - buy)
        return sold