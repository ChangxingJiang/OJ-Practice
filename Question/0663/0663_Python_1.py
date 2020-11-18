from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.vals = set()

    def checkEqualTree(self, root: TreeNode) -> bool:
        total = root.val + self.dfs(root.left) + self.dfs(root.right)  # 根节点不能是答案
        return total / 2 in self.vals

    def dfs(self, node):
        if node:
            v = node.val + self.dfs(node.left) + self.dfs(node.right)
            self.vals.add(v)
            return v
        else:
            return 0


if __name__ == "__main__":
    # True
    print(Solution().checkEqualTree(build_TreeNode([5, 10, 10, None, None, 2, 3])))

    # False
    print(Solution().checkEqualTree(build_TreeNode([1, 2, 10, None, None, 2, 20])))

    # False
    print(Solution().checkEqualTree(build_TreeNode([0, -1, 1])))
