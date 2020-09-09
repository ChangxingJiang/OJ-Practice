from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        pass


if __name__ == "__main__":
    # [1,2,3]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3])))

    # [4]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3, 4])))

    # [2,4,5]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3, 4, 5])))
