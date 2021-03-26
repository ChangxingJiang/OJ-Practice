from LeetTool import TreeNode
from LeetTool import build_TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.start = False
        self.parent = []
        self.now = None

    def hasNext(self) -> bool:
        if not self.start:
            return True
        else:
            if self.now.right:
                return True
            else:
                val = self.now.val
                for parent in self.parent:
                    if parent.val > val:
                        return True
                    if parent.right and parent.right.val > val:
                        return True
                return False

    def next(self) -> int:
        if self.start:
            if self.now.right:
                self.parent.append(self.now)
                self.now = self.now.right
                while self.now.left:
                    self.parent.append(self.now)
                    self.now = self.now.left
                return self.now.val
            else:
                val = self.now.val
                while self.parent:
                    self.now = self.parent.pop()
                    if self.now.val > val:
                        return self.now.val
                    if self.now.right and self.now.right.val > val:
                        self.parent.append(self.now)
                        self.now = self.now.right
                        while self.now.left:
                            self.parent.append(self.now)
                            self.now = self.now.left
                        return self.now.val
                return None
        else:
            self.start = True
            self.now = self.root
            while self.now.left:
                self.parent.append(self.now)
                self.now = self.now.left
            return self.now.val

    def hasPrev(self) -> bool:
        if not self.start:
            return False
        elif self.now.left:
            return True
        else:
            val = self.now.val
            for parent in self.parent:
                if parent.val < val:
                    return True
                if parent.left and parent.left.val < val:
                    return True
            return False

    def prev(self) -> int:
        if self.now.left:
            self.parent.append(self.now)
            self.now = self.now.left
            while self.now.right:
                self.parent.append(self.now)
                self.now = self.now.right
            return self.now.val
        else:
            val = self.now.val
            while self.parent:
                self.now = self.parent.pop()
                if self.now.val < val:
                    return self.now.val
                if self.now.left and self.now.left.val < val :
                    self.parent.append(self.now)
                    self.now = self.now.left
                    while self.now.right:
                        self.parent.append(self.now)
                        self.now = self.now.right
                    return self.now.val


if __name__ == "__main__":
    bst = BSTIterator(build_TreeNode([7, 3, 15, None, None, 9, 20]))
    print(bst.next())  # 3
    print(bst.next())  # 7
    print(bst.prev())  # 3
    print(bst.next())  # 7
    print(bst.hasNext())  # True
    print(bst.next())  # 9
    print(bst.next())  # 15
    print(bst.next())  # 20
    print(bst.hasNext())  # False
    print(bst.hasPrev())  # True
    print(bst.prev())  # 15
    print(bst.prev())  # 9
