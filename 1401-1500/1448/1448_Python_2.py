from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, last_max=-10001):
            if node:
                if node.val >= last_max:
                    self.ans += 1
                    dfs(node.left, node.val)
                    dfs(node.right, node.val)
                else:
                    dfs(node.left, last_max)
                    dfs(node.right, last_max)

        dfs(root)

        return self.ans


if __name__ == "__main__":
    # 4
    print(Solution().goodNodes(build_TreeNode([3, 1, 4, 3, None, 1, 5])))

    # 3
    print(Solution().goodNodes(build_TreeNode([3, 3, None, 4, 2])))

    # 1
    print(Solution().goodNodes(build_TreeNode([1])))
