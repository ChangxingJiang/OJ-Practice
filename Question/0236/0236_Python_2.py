from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 处理当前节点不存在的情况
        if not root:
            return root

        # 处理当前节点为p或q的情况
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 当左子树不包含目标节点时，返回右子树中找到的公共祖先
        if not left:
            return right

        # 当右子树不包含目标节点时，返回左子树中找到的公共祖先
        if not right:
            return left

        return root


if __name__ == "__main__":
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))  # 3
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right.right))  # 5
