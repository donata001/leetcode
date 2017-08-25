from collections import deque
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        #9：50
        if not k: return num
        stack = []
        for n in num:
            while k>0 and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        res = ''.join(stack)
        return res[:-k or None].lstrip('0') or '0'

#面对remove k啥的，带任何比较性质的求最大最小组合的都可以这么用，喜新厌旧

#similar to 316. Remove Duplicate Letters
