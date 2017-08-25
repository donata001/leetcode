class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_p = nums[0]
        min_p = nums[0]
        res = nums[0]
        for n in nums[1:]:
            old_max = max_p
            max_p = max([max_p*n, min_p*n, n])
            min_p = min([old_max*n, min_p*n, n])
            res = max(res, max_p)
        return res
            