from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.voyage = None
        self.ans = []
        self.i = 0

    def dfs(self, node):
        if node:
            # 处理根节点的值不相等的情况
            if node.val != self.voyage[self.i]:
                self.ans = [-1]
                return

            self.i += 1

            if node.left and self.i < len(self.voyage) and node.left.val != self.voyage[self.i]:
                self.ans.append(node.val)
                self.dfs(node.right)
                self.dfs(node.left)
            else:
                self.dfs(node.left)
                self.dfs(node.right)

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.voyage = voyage
        self.dfs(root)
        if self.ans and self.ans[0] == -1:
            return [-1]
        return self.ans


if __name__ == "__main__":
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2]), [2, 1]))  # [-1]
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2, 3]), [1, 3, 2]))  # [1]
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2, 3]), [1, 2, 3]))  # []
