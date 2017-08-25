class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        strs.sort()
        n = 0
        p, q = len(strs[0]),len(strs[-1])
        while n< min(p, q) and strs[0][n] == strs[-1][n]:
            n+=1
        return strs[0][:n]
