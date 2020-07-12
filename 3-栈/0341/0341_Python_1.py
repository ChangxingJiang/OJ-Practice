class NestedInteger:
    def __init__(self, data):
        pass

    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> "NestedInteger":
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


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
