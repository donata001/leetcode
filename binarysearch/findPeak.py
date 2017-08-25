class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(lo, hi):
            if hi== lo:
                return lo
            if hi-lo==1:
                return hi if nums[hi]>nums[lo] else lo
            # only when length>=3
            mid = (lo+hi)>>1
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid]<nums[mid+1]:
                return helper(mid+1, hi)
            else:
                return helper(lo, mid-1)

        return helper(0, len(nums)-1)


#注意这里用recursion是因为每次保证数量至少有3个