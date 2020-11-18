from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.idx = 0
        self.ans = 0

    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if node:
                dfs(node.right)
                self.idx += 1
                if self.idx == k:
                    self.ans = node.val
                    return
                dfs(node.left)

        dfs(root)

        return self.ans


if __name__ == "__main__":
    # 4
    print(Solution().kthLargest(build_TreeNode([3, 1, 4, None, 2]), 1))

    # 4
    print(Solution().kthLargest(build_TreeNode([5, 3, 6, 2, 4, None, None, 1]), 3))
