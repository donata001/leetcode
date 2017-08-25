class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = {}
        l,r, record = 0, 0, 0
        while r<len(s):
            mp[s[r]] = r
            if len(mp)>2:
                l = min(mp.values())
                mp.pop(s[l])
                l+=1
            record = max(record, r-l+1)
            r+=1
        return record

# 这题不用特别sliding window, 只要在map里面记录index
# r必须每轮都Increment