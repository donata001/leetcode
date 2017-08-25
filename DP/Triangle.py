class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #3:14
        if not triangle: return
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j ==0:
                    triangle[i][j] += triangle[i-1][j]
                elif j==len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])

# 典型的开头不知道，做完最后挑最小最大