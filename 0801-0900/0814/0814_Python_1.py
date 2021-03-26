from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.val == 1 or root.left or root.right:
                return root


if __name__ == "__main__":
    # [1,None,0,None,1]
    print(Solution().pruneTree(build_TreeNode([1, None, 0, 0, 1])))

    # [1,None,1,None,1]
    print(Solution().pruneTree(build_TreeNode([1, 0, 1, 0, 0, 0, 1])))

    # [1,1,0,1,1,None,1]
    print(Solution().pruneTree(build_TreeNode([1, 1, 0, 1, 1, 0, 1, 0])))
