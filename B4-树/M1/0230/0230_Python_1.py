from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().kthSmallest(build_TreeNode([3, 1, 4, None, 2]), 1))  # 1
    print(Solution().kthSmallest(build_TreeNode([5, 3, 6, 2, 4, None, None, 1]), 3))  # 3
