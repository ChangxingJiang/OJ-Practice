from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, min_val, max_val):
            if node:
                if node.val < min_val:
                    min_val = node.val
                elif node.val > max_val:
                    max_val = node.val
                self.ans = max(self.ans, max_val - min_val)
                dfs(node.left, min_val, max_val)
                dfs(node.right, min_val, max_val)

        dfs(root, root.val, root.val)
        return self.ans


if __name__ == "__main__":
    # 7
    print(Solution().maxAncestorDiff(build_TreeNode([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])))
