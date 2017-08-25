
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #8:59
        dp = [[0 for _ in xrange(len(s))] for _ in xrange(len(s))]
        res = ""
        for i in xrange(len(s)-1, -1, -1):
            for j in xrange(i, len(s)):
                dp[i][j] = s[i] == s[j] and (j-1<=i+1 or dp[i+1][j-1])
                if dp[i][j] and j-i+1>len(res):
                    res = s[i:j+1]
        return res

    def longestPalindrome1(self, s):
        def extenddp(i, j):
            while i>-1 and j <len(s) and s[i] == s[j]:
                i-=1
                j+=1
            if not self.res or self.res[1]-self.res[0] < j-i:
                self.res = [i, j]

        if len(s)< 2: return s
        self.res = []
        for i in xrange(len(s)-1):
            extenddp(i, i)
            extenddp(i, i+1)
        x, y = self.res
        return s[x+1:y]

    def longestPalindrome(self, s):
        maxv, start = 1, 0
        for i, ch in enumerate(s):
            if i>=maxv+1 and s[i-maxv-1:i+1] == s[i-maxv-1:i+1][::-1]:
                start = i-maxv-1
                maxv += 2
            elif i>=maxv and s[i-maxv:i+1] == s[i-maxv:i+1][::-1]:
                start = i-maxv
                maxv += 1

        return s[start:start+maxv]