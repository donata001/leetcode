class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # this method is finding insert point
        def search(nums, target):
            lo, hi = 0, len(nums) # insert point extended
            while lo < hi:
                m = (lo+hi)>>1
                if nums[m] >= target:
                    hi = m   # could be taget, don't move
                else:
                    lo = m+1
            return lo

        left = search(nums, target)
        return [left, search(nums, target+1)-1] if target in nums[left:left+1] else [-1,-1]
        # use slice instead of index to avoid index out of range

#通用寻找插入点