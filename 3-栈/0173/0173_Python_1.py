from toolkit import TreeNode, build_TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        pass

    def next(self) -> int:
        """
        @return the next smallest number
        """
        pass

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        pass


if __name__ == "__main__":
    root = build_TreeNode([7, 3, 15, None, None, 9, 20])
    obj = BSTIterator(root)
    print(obj.next())  # 3
    print(obj.next())  # 7
    print(obj.hasNext())  # True
    print(obj.next())  # 9
    print(obj.hasNext())  # True
    print(obj.next())  # 15
    print(obj.hasNext())  # True
    print(obj.next())  # 20
    print(obj.hasNext())  # False
