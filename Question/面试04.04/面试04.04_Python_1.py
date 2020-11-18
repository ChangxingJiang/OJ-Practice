from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(right - left) > 1:
            self.ans = False
        return max(left,right) + 1


if __name__ == "__main__":
    # True
    print(Solution().isBalanced(build_TreeNode([3, 9, 20, None, None, 15, 7])))

    # False
    print(Solution().isBalanced(build_TreeNode([1, 2, 2, 3, 3, None, None, 4, 4])))
