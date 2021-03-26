from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            s1, n1 = self.dfs(node.left)
            s2, n2 = self.dfs(node.right)
            s, n = s1 + s2 + node.val, n1 + n2 + 1
            self.ans = max(self.ans, s / n)
            return s, n
        else:
            return 0, 0


if __name__ == "__main__":
    # 6.00000
    print(Solution().maximumAverageSubtree(build_TreeNode([5, 6, 1])))
