class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # step1, find 一个顺序最大的index
        i = len(nums)-2  #找前面那个数    14218， 找到第二个1，然后第二步找到8
        while i> -1:
            if nums[i]<nums[i+1]:
                break
            i-=1
        # 如果没有，sort return
        if i == -1:
            nums.sort()
            return

        #step2, find 一个比nums[i]大的最大index l
        j = len(nums)-1
        while j>-1:
            if nums[j]>nums[i]:
                break
            j-=1
        #step3 swap i, j value
        nums[i], nums[j] = nums[j], nums[i]
        #step 4, reverse i+1:
        nums[i+1:] = nums[i+1:][::-1]

