class Solution(object):
    def permute1(self, nums):
        def dfs(res):
            if len(res) == len(nums):
                result.append(res)
                return
            for i in xrange(len(nums)):
                if nums[i] not in res: #问清楚有没有重复
                    dfs(res+[nums[i]])

        result = []
        dfs([])
        return result

    #BFS  适用于全排列
    def permute(self, nums):
        q, next = [[]], []   #seq从[]一直成长到len(num)
        for n in nums:
            for seq in q:
                for i in xrange(len(seq)+1):
                    next.append(seq[:i] + [n] + seq[i:])
            q, next = next, []
        return q

    # 如果有相同的情况
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        q, next = [[]], []
        for n in nums:
            for seq in q:
                for i in xrange(len(seq)+1):
                    next.append(seq[:i] + [n] + seq[i:])
                    if i<len(seq) and n == seq[i]:
                        break
                        #allow第一次插入左边，然后所有的插入都重复，就break
                        #因为q里面的都是同一个n各个位置插过了
            q, next = next, []
        return q
