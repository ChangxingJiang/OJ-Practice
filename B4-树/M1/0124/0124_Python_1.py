from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxPathSum(build_TreeNode([1, 2, 3])))  # 6
    print(Solution().maxPathSum(build_TreeNode([-10, 9, 20, None, None, 15, 7])))  # 42
