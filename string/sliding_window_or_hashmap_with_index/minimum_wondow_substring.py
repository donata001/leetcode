from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #5:33
        l, r, counter, m, record, res = 0, 0, len(t), Counter(t), float("INF"), ""
        while r < len(s):
            if m[s[r]] >0:
                counter -= 1
            m[s[r]] -= 1
            r+=1
            while counter == 0:
                if record >= r-l+1:
                    record = r-l+1
                    res = s[l:r]
                if m[s[l]] >= 0:
                    counter += 1
                m[s[l]]+=1
                l+=1
        return res

