from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]

        if V < root.val:
            left, right = self.splitBST(root.left, V)
            root.left = right
            return [left, root]
        elif root.val < V:
            left, right = self.splitBST(root.right, V)
            root.right = left
            return [root, right]
        else:
            right = root.right
            root.right = None
            return [root, right]


if __name__ == "__main__":
    # [[2,1],[4,3,6,null,null,5,7]]
    print(Solution().splitBST(build_TreeNode([4, 2, 6, 1, 3, 5, 7]), 2))
