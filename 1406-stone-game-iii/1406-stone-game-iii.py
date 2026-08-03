class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n=len(stoneValue)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            sum=0
            dp[i]=float('-inf')
            for j in range(i,min((i+3),n)):
                sum+=stoneValue[j]
                dp[i]=max(dp[i],sum-dp[j+1])
        if dp[i]>0:
            return "Alice"
        elif dp[i]<0:
            return "Bob"
        else:
            return "Tie"
        