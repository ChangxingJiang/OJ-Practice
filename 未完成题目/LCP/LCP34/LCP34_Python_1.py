from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxValue(root=build_TreeNode([5, 2, 3, 4]), k=2))  # 12
    print(Solution().maxValue(root=build_TreeNode([4, 1, 3, 9, None, None, 2]), k=2))  # 16
