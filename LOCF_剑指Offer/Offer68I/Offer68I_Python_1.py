from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


if __name__ == "__main__":
    # 6
    tree = build_TreeNode([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))

    # 2
    tree = build_TreeNode([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right))
