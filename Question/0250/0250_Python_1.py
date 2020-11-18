from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.dfs(root)

        return self.ans

    def dfs(self, node):
        if node.left and node.right:
            v1 = self.dfs(node.left)
            v2 = self.dfs(node.right)
            if v1 is not None and v2 is not None and node.val == v1 == v2:
                self.ans += 1
                return node.val
            else:
                return None
        elif node.left:
            v = self.dfs(node.left)
            if v is not None and node.val == v:
                self.ans += 1
                return node.val
            else:
                return None
        elif node.right:
            v = self.dfs(node.right)
            if v is not None and node.val == v:
                self.ans += 1
                return node.val
            else:
                return None
        else:
            self.ans += 1
            return node.val


if __name__ == "__main__":
    # 4
    print(Solution().countUnivalSubtrees(build_TreeNode([5, 1, 5, 5, 5, None, 5])))
