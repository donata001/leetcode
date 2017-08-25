class Solution(object):
    # TLE
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def dfs(idx):
            if idx == len(s): return True
            for i in xrange(idx+1, len(s)+1):
                if s[idx:i] in wordDict and dfs(i):
                    return True
            return False

        if not s or not wordDict: return False
        wordDict = set(wordDict)
        return dfs(0)
    #DP
    def wordBreak(self, s, wordDict):
        dp = [False for _ in xrange(len(s)+1)]
        dp[0] = True
        wordDict = set(wordDict)
        for i, c in enumerate(s):
            dp[i+1] = any(dp[x] and s[x:i+1] in wordDict for x in xrange(i+1))

        return dp[-1]
        