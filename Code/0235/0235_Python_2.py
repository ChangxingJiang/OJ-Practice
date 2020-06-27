from toolkit import TreeNode, build_TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
                continue
            if p.val < root.val and q.val < root.val:
                root = root.left
                continue
            else:
                return root


if __name__ == "__main__":
    tree = build_TreeNode([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))  # 6
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right))  # 2
