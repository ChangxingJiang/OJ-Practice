from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = []

    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node.left and node.right:
            self.dfs(node.left)
            self.dfs(node.right)
        elif node.left:
            self.ans.append(node.left.val)
            self.dfs(node.left)
        elif node.right:
            self.ans.append(node.right.val)
            self.dfs(node.right)


if __name__ == "__main__":
    # [4]
    print(Solution().getLonelyNodes(build_TreeNode([1, 2, 3, None, 4])))

    # [6,2]
    print(Solution().getLonelyNodes(build_TreeNode([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2])))

    # [77,55,33,66,44,22]
    print(Solution().getLonelyNodes(
        build_TreeNode([11, 99, 88, 77, None, None, 66, 55, None, None, 44, 33, None, None, 22])))

    # []
    print(Solution().getLonelyNodes(build_TreeNode([197])))

    # [78,28]
    print(Solution().getLonelyNodes(build_TreeNode([31, None, 78, None, 28])))
