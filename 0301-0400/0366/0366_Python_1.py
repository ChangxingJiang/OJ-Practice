from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = []

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            height = 1 + max(self.dfs(node.left), self.dfs(node.right))
            if len(self.ans) < height:
                self.ans.append([])
            self.ans[height - 1].append(node.val)
            return height
        else:
            return 0


if __name__ == "__main__":
    # [[4,5,3],[2],[1]]
    print(Solution().findLeaves(build_TreeNode([1, 2, 3, 4, 5])))
