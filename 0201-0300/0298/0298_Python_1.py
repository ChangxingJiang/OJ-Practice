from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.dfs(root, 0, float("NAN"))
        return self.ans

    def dfs(self, node, now_length, now_val):
        if node:
            if node.val == now_val + 1:
                self.ans = max(self.ans, now_length + 1)
                self.dfs(node.left, now_length + 1, node.val)
                self.dfs(node.right, now_length + 1, node.val)
            else:
                self.ans = max(self.ans, 1)
                self.dfs(node.left, 1, node.val)
                self.dfs(node.right, 1, node.val)


if __name__ == "__main__":
    # 3
    print(Solution().longestConsecutive(build_TreeNode([1, None, 3, 2, 4, None, None, None, 5])))

    # 2
    print(Solution().longestConsecutive(build_TreeNode([2, None, 3, 2, None, 1])))
