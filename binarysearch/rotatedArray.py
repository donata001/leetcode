class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        # step1 find real beginning
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid]>nums[hi]: # all unique
                lo = mid+1
            else:
                hi = mid

        #step 2 nornal binary search with shift
        # 三个pointer全部都是一样的shift，所以全部原操作
        l, h = 0, len(nums)-1
        while l<=h: # length为1，一般情况下不要等
            mid = (l+h)//2
            real_m = (mid+lo)%len(nums)
            if nums[real_m]==target:
                return real_m
            if nums[real_m]>target:
                h = mid-1
            else:
                l = mid+1

        return -1


    # 有重复元素
    def search(self, nums, target):
        if not nums: return False
        lo, hi = 0, len(nums)-1
        while lo<hi:
            if nums[lo]<nums[hi]:
                break
            mid = (lo+hi)/2
            if nums[mid]>nums[hi]:
                lo = mid+1
            elif nums[mid]<nums[hi]:
                hi = mid
            else:
                hi -=1   #trick，适用于不好决定挪一挪再说
        l, h = 0, len(nums)-1
        while l<=h:
            m = (l+h)>>1
            real_m = (m+lo)%len(nums)
            if nums[real_m]==target:
                return True
            if nums[real_m]<target:
                l = m+1
            else:
                h = m-1
        return False