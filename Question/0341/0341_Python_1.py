# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, params):
        pass

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            self.stack += self.stack.pop().getList()[::-1]
        return self.stack != []


if __name__ == "__main__":
    nested_int = NestedInteger([[1, 1], 2, [1, 1]])
    nested_iter = NestedIterator(nested_int)
    ans = []
    while nested_iter.hasNext():
        ans.append(nested_iter.next())
    print(ans)  # [1,1,2,1,1]

    nested_int = NestedInteger([1, [4, [6]]])
    nested_iter = NestedIterator(nested_int)
    ans = []
    while nested_iter.hasNext():
        ans.append(nested_iter.next())
    print(ans)  # [1,4,6]
