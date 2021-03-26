import collections
from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.sub_trees = collections.Counter()
        self.ans = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def recursor(node):
            if not node:
                return ""
            if node.left and node.right:
                expression = str(node.val) + ":[" + recursor(node.left) + "," + recursor(node.right) + "]"
            elif node.left:
                expression = str(node.val) + ":[" + recursor(node.left) + ",]"
            elif node.right:
                expression = str(node.val) + ":[," + recursor(node.right) + "]"
            else:
                expression = str(node.val) + ":[,]"
            if self.sub_trees[expression] == 1:
                self.ans.append(node)
            self.sub_trees[expression] += 1
            return expression

        recursor(root)
        return self.ans


if __name__ == "__main__":
    # [[2,4],[4]]
    tree = build_TreeNode([1, 2, 3, 4, None, 2, 4, None, None, 4])
    print(Solution().findDuplicateSubtrees(tree))
