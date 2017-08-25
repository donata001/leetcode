class Solution(object):
    def numDecodings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        #11:29
        if not s: return 0
        dp = [0 for _ in xrange(len(s)+1)]
        dp[-1] = 1 # 代表空string, 另外一般情况下如果不能决定DP[0]就多加一个base
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] = dp[i+1]
            if i<len(s)-1 and 10<=int(s[i:i+2])<27:# 如果是10, 20的情况dp[i+1]是0，所以直接拿i+2
                dp[i] += dp[i+2]

        return dp[0]

    def numDecodings(self, s):
        if not s or s[0]=="0": return 0
        r1, r2 = 1, 1
        for i in xrange(1, len(s)):
            if s[i] == '0':
                r1 = 0
            if 10<=int(s[i-1:i+1])<27:
                r1 = r1+r2
                r2 = r1-r2
            else:
                r2 = r1
        return r1




            