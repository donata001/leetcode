class Solution(object):
    def decodeString1(self, s):
        def helper(i):
            res = ''
            while i<len(s) and s[i]!=']': #只做一层内的
                if s[i].isalpha():
                    res += s[i]
                else:
                    digit = ''
                    while i<len(s) and s[i].isdigit():
                        digit += s[i]
                        i+=1
                    i+=1
                    string, idx = helper(i)
                    res+= int(digit)*string
                    i = idx
                i+=1
            return res, i
        return helper(0)[0]

    def decodeString2(self, s):
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]+)\]', lambda x: int(x.group(1))*x.group(2), s)
        return s

    def decodeString(self, s):
        stack = []
        num = ''
        stack.append(["", 1])   # 处理开头就是字母的case
        for ch in s:
            if ch.isdigit():
                num+=ch
            elif ch.isalpha():
                stack[-1][0]+=ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ''
            elif ch == ']':
                string, n = stack.pop() # 层关系用stack时结束一层用pop
                stack[-1][0]+=string*n
        return stack[0][0]


