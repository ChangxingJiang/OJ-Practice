from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().countPairs(build_TreeNode([1, 2, 3, None, 4]), 3))  # 1
    print(Solution().countPairs(build_TreeNode([1, 2, 3, 4, 5, 6, 7]), 3))  # 2
    print(Solution().countPairs(build_TreeNode([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]), 3))  # 1
    print(Solution().countPairs(build_TreeNode([1100]), 1))  # 0
    print(Solution().countPairs(build_TreeNode([1, 1, 1]), 2))  # 1
