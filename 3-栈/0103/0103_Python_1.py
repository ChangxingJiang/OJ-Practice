from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [
    #   [3],
    #   [20,9],
    #   [15,7]
    # ]
    print(Solution().zigzagLevelOrder(build_TreeNode([3, 9, 20, None, None, 15, 7])))
