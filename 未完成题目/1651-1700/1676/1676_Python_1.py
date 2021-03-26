from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        pass


if __name__ == "__main__":
    # 2
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, [tree.left.right.left, tree.left.right.right]))

    # 1
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, [tree.right]))

    # 5
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, [tree.left.right.left, tree.left.left, tree.left.right,
                                                 tree.left.right.right]))

    # 3
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree,
                                          [tree.right.left, tree.right, tree.left.right, tree, tree.left.right.right,
                                           tree.left, tree.left.left, tree.left.right.left, tree.right.right]))
