class Solution(object):
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #3:39
        if not nums: return 0
        dp = [1 for _ in xrange(len(nums))] # 最少是1
        for i, n in enumerate(nums[1:], 1):
            record = 1
            for j, m in enumerate(nums[:i]):
                #如果不存在比它小的数，保持原来的
                if m < n:
                    record = max(record, dp[j]) #踩着前面人的尸体
                    dp[i] = record+1
        return max(dp)  #不同于一般dp，取最大

    def lengthOfLIS(self, nums):
        tailing = [0 for _ in xrange(len(nums))]
        size = 0

        for n in nums:
            i, j = 0, size
            while i< j:
                m = (i+j)>>1
                if tailing[m] < n:
                    i = m+1
                else:
                    j = m
            tailing[i] = n
            size = max(size, i+1)
        return size




