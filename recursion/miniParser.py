# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize1(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        #11：56
        def helper(x):
            if isinstance(x, int):
                return NestedInteger(x)
            n = NestedInteger()
            for ch in x:
                n.add(helper(ch))
            return n

        return helper(eval(s))

    def deserialize(self, s):
        def helper():
            num = ''
            while x[-1] in '0123456789-':
                num += x.pop()
            if num: return NestedInteger(int(num))
            if x[-1] == '[':
                x.pop()
            n = NestedInteger()
            while x[-1] != ']': #最关键的一个loop，所有recursion share一个list， helper不停做reduce
                n.add(helper()) # 如果有nested list，层内迭代在这里
                if x[-1] == ',':
                    x.pop()
            x.pop()  # pop掉 】
            return n
        x = list(' ' + s[::-1])   # 为了最后一个while check x[-1]
        return helper()

        