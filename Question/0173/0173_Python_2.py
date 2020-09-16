from toolkit import TreeNode, build_TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        ans = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return ans

    def hasNext(self) -> bool:
        return self.stack != []


if __name__ == "__main__":
    tree = build_TreeNode([7, 3, 15, None, None, 9, 20])
    obj = BSTIterator(tree)
    print(obj.next())  # 3
    print(obj.next())  # 7
    print(obj.hasNext())  # True
    print(obj.next())  # 9
    print(obj.hasNext())  # True
    print(obj.next())  # 15
    print(obj.hasNext())  # True
    print(obj.next())  # 20
    print(obj.hasNext())  # False
