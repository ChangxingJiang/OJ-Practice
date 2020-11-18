from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def maybe_find(self, n1, n2):
        if not n1 and not n2:
            return True
        elif not n1 or not n2:
            return False
        elif n1.val != n2.val:
            return False
        else:
            return self.maybe_find(n1.left, n2.left) and self.maybe_find(n1.right, n2.right)

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True
        elif not t1:
            return False
        elif t1.val == t2.val and self.maybe_find(t1, t2):
            return True
        else:
            return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)


if __name__ == "__main__":
    # True
    print(Solution().checkSubTree(build_TreeNode([1, 2, 3]), build_TreeNode([2])))

    # False
    print(Solution().checkSubTree(build_TreeNode([1, None, 2, 4]), build_TreeNode([3, 2])))
