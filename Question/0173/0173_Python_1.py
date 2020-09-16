from toolkit import TreeNode, build_TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        stack = [root]
        self.ans = []
        while stack:
            node = stack[-1]
            if node:
                stack.append(node.left)
            else:
                stack.pop()
                if not stack:
                    break
                now = stack.pop()
                self.ans.append(now.val)
                stack.append(now.right)
            print(stack)

    def next(self) -> int:
        return self.ans.pop(0)

    def hasNext(self) -> bool:
        return len(self.ans) > 0


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
