import collections
from typing import List

from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.min_idx = 0
        self.max_idx = 0
        self.ans = collections.deque([[]])

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        self.dfs(root, 0, 0)

        ans = []
        for level in self.ans:
            level.sort(key=lambda x: x[0])
            ans.append([elem[1] for elem in level])

        return ans

    def dfs(self, node, idx, h):
        if node:
            if idx < self.min_idx:
                self.min_idx -= 1
                self.ans.appendleft([])
            elif idx > self.max_idx:
                self.max_idx += 1
                self.ans.append([])
            actual_idx = idx - self.min_idx
            self.ans[actual_idx].append((h, node.val))

            self.dfs(node.left, idx - 1, h + 1)
            self.dfs(node.right, idx + 1, h + 1)


if __name__ == "__main__":
    # [
    #   [9],
    #   [3,15],
    #   [20],
    #   [7]
    # ]
    print(Solution().verticalOrder(build_TreeNode([3, 9, 20, None, None, 15, 7])))

    # [
    #   [4],
    #   [9],
    #   [3,0,1],
    #   [8],
    #   [7]
    # ]
    print(Solution().verticalOrder(build_TreeNode([3, 9, 8, 4, 0, 1, 7])))

    # [
    #   [4],
    #   [9,5],
    #   [3,0,1],
    #   [8,2],
    #   [7]
    # ]
    print(Solution().verticalOrder(build_TreeNode([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])))
