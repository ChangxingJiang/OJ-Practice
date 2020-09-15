from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node, last=0):
            if node:
                last ^= 1 << (node.val - 1)
                if node.left or node.right:
                    dfs(node.left, last)
                    dfs(node.right, last)
                else:
                    num = 0
                    while last:
                        num += last & 1
                        last >>= 1
                    if num <= 1:
                        self.ans += 1

        dfs(root)

        return self.ans


if __name__ == "__main__":
    # 2
    print(Solution().pseudoPalindromicPaths(build_TreeNode([2, 3, 1, 3, 1, None, 1])))

    # 1
    print(Solution().pseudoPalindromicPaths(build_TreeNode([2, 1, 1, 1, 3, None, None, None, None, None, 1])))

    # 1
    print(Solution().pseudoPalindromicPaths(build_TreeNode([9])))
