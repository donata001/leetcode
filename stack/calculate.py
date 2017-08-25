class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #10:47
        op = []
        num = ''
        sign = "+" #第一个数字
        s = s.strip()
        for i, c in enumerate(s):
            if c.isdigit():
                num += c
            if c in '+-*/' or i == len(s) -1: #last one don't wait for next ch
                if sign == "+":
                    op.append(int(num))
                elif sign == "-":
                    op.append(-int(num))
                elif sign == "*":
                    op.append(int(num)*op.pop())
                elif sign == '/':
                    #python 2 specific
                    a,b = op.pop(), int(num)
                    res = a/b if a/b>=0 else -(-a/b)
                    op.append(res)
                sign = c
                num = ''

        return reduce(lambda x, y: x+y, op)

#push signed value，遇到高阶的pop出一个先算



