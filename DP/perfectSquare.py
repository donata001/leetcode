class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("INF") for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        i = 2
        while i <n+1:
            dp[i] = min(dp[i-j*j]+1 for j in xrange(int(i**0.5)+1))
            i+=1
        return dp[-1]