from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[9],[3,15],[20],[7]]
    print(Solution().verticalTraversal(build_TreeNode([3, 9, 20, None, None, 15, 7])))

    # [[4],[2],[1,5,6],[3],[7]]
    print(Solution().verticalTraversal(build_TreeNode([1, 2, 3, 4, 5, 6, 7])))
