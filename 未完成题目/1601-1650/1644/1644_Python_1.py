from LeetTool import TreeNode
from LeetTool import build_TreeNode


# Definition for a binary tree node.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass


if __name__ == "__main__":
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))  # 3

    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right.right))  # 5

    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    node2 = TreeNode(10)
    print(Solution().lowestCommonAncestor(tree, tree.left, node2))  # None
