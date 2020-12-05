from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        pass


if __name__ == "__main__":
    # [1,2,3,4,null,null,7,8,9,null,14]
    print(Solution().sufficientSubset(build_TreeNode([[1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]]), 1))

    # [5,4,8,11,null,17,4,7,null,null,null,5]
    print(Solution().sufficientSubset(build_TreeNode([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]), 22))

    # []
    print(Solution().sufficientSubset(build_TreeNode([5, -6, -6]), 0))
