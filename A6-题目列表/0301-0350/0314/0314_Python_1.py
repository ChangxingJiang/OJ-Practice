from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [
    #   [9],
    #   [3,15],
    #   [20],
    #   [7]
    # ]
    print(Solution().verticalOrder(build_TreeNode([3, 9, 20, None, None, 15, 7])))

    # [
    #   [4],
    #   [9],
    #   [3,0,1],
    #   [8],
    #   [7]
    # ]
    print(Solution().verticalOrder(build_TreeNode([3, 9, 8, 4, 0, 1, 7])))

    # [
    #   [4],
    #   [9,5],
    #   [3,0,1],
    #   [8,2],
    #   [7]
    # ]
    print(Solution().verticalOrder(build_TreeNode([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])))
