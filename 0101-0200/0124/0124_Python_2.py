from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        MOD = 10 ** 9 + 7
        self.max = -MOD

    def maxPathSum(self, root: TreeNode) -> int:
        self.count_max(root)
        return self.max

    def count_max(self, node: TreeNode) -> int:
        if not node:
            return 0

        left_max = max(self.count_max(node.left), 0)
        right_max = max(self.count_max(node.right), 0)

        self.max = max(self.max, node.val + left_max + right_max)  # 更新最大路径和

        return node.val + max(left_max, right_max)  # 生成返回值


if __name__ == "__main__":
    print(Solution().maxPathSum(build_TreeNode([1, 2, 3])))  # 6
    print(Solution().maxPathSum(build_TreeNode([-10, 9, 20, None, None, 15, 7])))  # 42
    print(Solution().maxPathSum(build_TreeNode([2, -1])))  # 2
