from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.total = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.total += root.val
            root.val = self.total
            self.bstToGst(root.left)

        return root


if __name__ == "__main__":
    print(Solution().bstToGst(build_TreeNode([5, 2, 13])))  # [18,20,13]
