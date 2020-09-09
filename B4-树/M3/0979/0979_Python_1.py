from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    print(Solution().distributeCoins(build_TreeNode([3, 0, 0])))  # 2
    print(Solution().distributeCoins(build_TreeNode([0, 3, 0])))  # 3
    print(Solution().distributeCoins(build_TreeNode([1, 0, 2])))  # 2
    print(Solution().distributeCoins(build_TreeNode([1, 0, 0, None, 3])))  # 4
