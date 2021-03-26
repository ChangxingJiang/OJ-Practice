# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 处理只是一个整数的情况
        if s[0] != "[":
            return NestedInteger(int(s))

        # 处理一个空列表的情况
        elif s == "[]":
            return NestedInteger()

        # 处理一个列表的情况
        else:
            ans = NestedInteger()
            s = s[1:-1]
            num = 0
            last = 0
            for i in range(len(s)):
                if s[i] == "," and num == 0:
                    ans.add(self.deserialize(s[last:i]))
                    last = i + 1
                elif s[i] == "[":
                    num += 1
                elif s[i] == "]":
                    num -= 1
            ans.add(self.deserialize(s[last:]))
            return ans


if __name__ == "__main__":
    print(Solution().deserialize("324"))  # 324
    print(Solution().deserialize("[123,[456,[789]]]"))  # [123,[456,[789]]]
