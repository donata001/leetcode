class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        l, r = 0, 0
        record = {}
        while r<len(s):
            if s[r] in record:
                l = max(l, record[s[r]]+1)
            record[s[r]] = r
            res = max(res, r-l+1)
            r+=1
        return res

# map里面仍然记录index， 两种情况，l已经pass那个重的，或者l没有
#pass，either情况取个max就可以避免，然后再跟新r的index，顺序不要反了

#sliding window也可以做