class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #4:26
        dp = [[0 for _ in xrange(len(word1)+1)] for _ in xrange(len(word2)+1)]
        dp[0] = range(len(word1)+1)
        for j in xrange(len(dp)):
            dp[j][0] = j
        for i, w1 in enumerate(word2, 1):
            for j, w2 in enumerate(word1, 1):
                if w1 == w2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1  #两个不同的string match
        return dp[-1][-1]