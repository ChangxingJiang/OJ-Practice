from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if node.left and node.right:
                left = dfs(node.left)
                right = dfs(node.right)
                for i in range(distance - 1):
                    for j in range(0, distance - 1 - i):
                        self.ans += left[i] * right[j]
                return [0] + [left[i] + right[i] for i in range(distance - 1)]
            elif node.left:
                left = dfs(node.left)
                return [0] + left[:-1]
            elif node.right:
                right = dfs(node.right)
                return [0] + right[:-1]
            else:
                return [1] + [0] * (distance - 2)

        dfs(root)

        return self.ans


if __name__ == "__main__":
    print(Solution().countPairs(build_TreeNode([1, 2, 3, None, 4]), 3))  # 1
    print(Solution().countPairs(build_TreeNode([1, 2, 3, 4, 5, 6, 7]), 3))  # 2
    print(Solution().countPairs(build_TreeNode([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]), 3))  # 1
    print(Solution().countPairs(build_TreeNode([1100]), 1))  # 0
    print(Solution().countPairs(build_TreeNode([1, 1, 1]), 2))  # 1
