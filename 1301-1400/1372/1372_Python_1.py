from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.max = 0

    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            if node.left and node.right:
                left = dfs(node.left)[1]
                right = dfs(node.right)[0]
                self.max = max(self.max, left, right)
                return left + 1, right + 1
            elif node.left:
                left = dfs(node.left)[1]
                right = 0
                self.max = max(self.max, left)
                return left + 1, right + 1
            elif node.right:
                left = 0
                right = dfs(node.right)[0]
                self.max = max(self.max, right)
                return left + 1, right + 1
            else:
                return 1, 1

        dfs(root)

        return self.max


if __name__ == "__main__":
    # 3
    print(Solution().longestZigZag(build_TreeNode([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1])))

    # 4
    print(Solution().longestZigZag(build_TreeNode([1, 1, 1, None, 1, None, None, 1, 1, None, 1])))

    # 0
    print(Solution().longestZigZag(build_TreeNode([1])))
