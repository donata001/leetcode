from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        res = []
        for i, n in enumerate(nums):
            if dq and dq[0]<i-k+1:   #最左侧存的index是否还在window
                dq.popleft()
            while dq and nums[dq[-1]]<=n:   #扫光左侧所有比incoming小的
                dq.pop()
            dq.append(i)
            if i>=k-1: res.append(nums[dq[0]]) #长度够window
        return res