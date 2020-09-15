from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.max = 0

    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0

            if node.left:
                left = dfs(node.left)[1]
            else:
                left = 0

            if node.right:
                right = dfs(node.right)[0]
            else:
                right = 0

            self.max = max(self.max, left, right)

            return left + 1, right + 1

        dfs(root)

        return self.max


if __name__ == "__main__":
    # 3
    print(Solution().longestZigZag(build_TreeNode([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1])))

    # 4
    print(Solution().longestZigZag(build_TreeNode([1, 1, 1, None, 1, None, None, 1, 1, None, 1])))

    # 0
    print(Solution().longestZigZag(build_TreeNode([1])))
