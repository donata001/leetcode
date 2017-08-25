class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def helper(idx, target, res):
            if target<0:
                return
            if target==0:
                result.append(res)
                return
            for i in xrange(idx, len(candidates)):
                if i >idx and candidates[i]==candidates[i-1]:  #有重复的处理，只是avoid了同一个level的
                    continue
                helper(i+1, target-candidates[i], res+[candidates[i]])
        candidates.sort()
        helper(0, target, [])
        return result

# 一旦idx比第一个重复元素的index大，就不是问题了，因为这个不同于permutation，它只从剩下的slice里面取