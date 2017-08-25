class Solution(object):
    def findNthDigit(self, n):
        # 1-9 9
        # 10-99 90
        # 100-999 1000-100
        # 1000-9999 10000-1000

        level, bucket, start = 1, 9, 1
        while n > level*bucket:
            n -= level*bucket
            level += 1
            bucket *= 10
            start *= 10
        return int(str(start+(n-1)/level)[(n-1)%level])
        #                          层数也是每个数占的位数
