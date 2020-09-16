from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
            return root


if __name__ == "__main__":
    # [4,7,2,9,6,3,1]
    print(Solution().mirrorTree(build_TreeNode([4, 2, 7, 1, 3, 6, 9])))
