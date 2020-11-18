from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.arr = []

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.arr = arr
        return self.dfs(root, 0)

    def dfs(self, node, i):
        if node and i < len(self.arr) and node.val == self.arr[i]:
            if i == len(self.arr)-1 and not node.left and not node.right:
                return True
            else:
                return self.dfs(node.left, i + 1) or self.dfs(node.right, i + 1)
        else:
            return False


if __name__ == "__main__":
    # True
    print(Solution().isValidSequence(build_TreeNode([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), [0, 1, 0, 1]))

    # False
    print(Solution().isValidSequence(build_TreeNode([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), [0, 0, 1]))

    # False
    print(Solution().isValidSequence(build_TreeNode([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), [0, 1, 1]))

    # False
    print(Solution().isValidSequence(build_TreeNode([2, 9, 3, None, 1, None, 2, None, 8]), [2, 9, 1, 8, 0]))
