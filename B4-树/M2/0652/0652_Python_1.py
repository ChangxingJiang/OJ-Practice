from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        pass


if __name__ == "__main__":
    # [[2,4],[4]]
    tree = build_TreeNode([1, 2, 3, 4, None, 2, 4, None, None, 4])
    print(Solution().findDuplicateSubtrees(tree))
