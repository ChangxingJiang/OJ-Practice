from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root:
            return 0
        else:
            left = self.dfs(root.left, p, q)
            right = self.dfs(root.right, p, q)
            this = 1 if root == p or root == q else 0
            if left == 2 or right == 2:
                return 2
            elif (left + right + this) == 2:
                self.ans = root
                return 2
            else:
                return left + right + this


if __name__ == "__main__":
    # 3
    head = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(head, head.left, head.right))

    # 4
    head = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(head, head.left, head.left.right.right))
