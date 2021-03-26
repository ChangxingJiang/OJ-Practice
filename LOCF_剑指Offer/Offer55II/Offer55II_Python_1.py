from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.ans = False
            return max(left, right) + 1

        dfs(root)

        return self.ans


if __name__ == "__main__":
    # True
    print(Solution().isBalanced(build_TreeNode([3, 9, 20, None, None, 15, 7])))

    # False
    print(Solution().isBalanced(build_TreeNode([1, 2, 2, 3, 3, None, None, 4, 4])))
