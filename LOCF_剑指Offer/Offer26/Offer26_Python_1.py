from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        def dfs1(a):
            if a:
                if a.val == B.val:
                    if dfs2(a.left, B.left) and dfs2(a.right, B.right):
                        self.ans = True
                dfs1(a.left)
                dfs1(a.right)

        def dfs2(a, b):
            if a and b:
                return a.val == b.val and dfs2(a.left, b.left) and dfs2(a.right, b.right)
            elif a:
                return True
            elif b:
                return False
            else:
                return True

        dfs1(A)

        return self.ans


if __name__ == "__main__":
    print(Solution().isSubStructure(build_TreeNode([1, 2, 3]), build_TreeNode([3, 1])))  # False
    print(Solution().isSubStructure(build_TreeNode([3, 4, 5, 1, 2]), build_TreeNode([4, 1])))  # True
