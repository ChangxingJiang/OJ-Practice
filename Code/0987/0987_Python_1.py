import collections
from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = collections.defaultdict(list)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, idx, level):
            if node:
                self.ans[idx].append((node.val, level))
                if node.left:
                    dfs(node.left, idx - 1, level + 1)
                if node.right:
                    dfs(node.right, idx + 1, level + 1)

        dfs(root, 0, 0)
        ans = []
        for k in sorted(self.ans.keys()):
            ans.append([elem[0] for elem in sorted(self.ans[k], key=lambda x: (x[1], x[0]))])
        return ans


if __name__ == "__main__":
    # [[9],[3,15],[20],[7]]
    print(Solution().verticalTraversal(build_TreeNode([3, 9, 20, None, None, 15, 7])))

    # [[4],[2],[1,5,6],[3],[7]]
    print(Solution().verticalTraversal(build_TreeNode([1, 2, 3, 4, 5, 6, 7])))
