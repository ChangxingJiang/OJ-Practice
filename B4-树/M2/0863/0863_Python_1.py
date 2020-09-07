from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        pass


if __name__ == "__main__":
    # [7,4,1]
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().distanceK(tree, tree.left, 2))
