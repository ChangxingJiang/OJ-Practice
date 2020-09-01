from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [
    #   [3],
    #   [9,20],
    #   [15,7]
    # ]
    print(Solution().levelOrder(build_TreeNode([3, 9, 20, None, None, 15, 7])))
