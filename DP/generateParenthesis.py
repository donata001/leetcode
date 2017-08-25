class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #9:41
        def helper(left, right, path):
            if left+right == 2*n:
                res.append(path)
                return

            if left < n:
                helper(left+1, right, path + '(')
            if left > right:
                helper(left, right+1, path +')')

        res = []
        helper(0, 0, '')
        return res

                