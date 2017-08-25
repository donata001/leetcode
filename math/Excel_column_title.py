class Solution:
    def convertToTitle(self, n):
        res = ''
        while n>0:
            n-=1
            res+=chr(ord('A')+n%26)
            n/=26
        return res[::-1]

# 总结类似进制转换的问题，首先观察是否index从0开始，不是的话每一轮先map回去