from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += abs(left) + abs(right)
            return left + right + (node.val - 1)

        dfs(root)
        return self.ans


if __name__ == "__main__":
    print(Solution().distributeCoins(build_TreeNode([3, 0, 0])))  # 2
    print(Solution().distributeCoins(build_TreeNode([0, 3, 0])))  # 3
    print(Solution().distributeCoins(build_TreeNode([1, 0, 2])))  # 2
    print(Solution().distributeCoins(build_TreeNode([1, 0, 0, None, 3])))  # 4
