from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root:
            if root == p or root == q:
                return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if not left:
                return right
            if not right:
                return left
            return root


if __name__ == "__main__":
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))  # 3
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right.right))  # 5
