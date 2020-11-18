from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, pp, qq):
            if node:
                now = dfs(node.left, pp, qq) + dfs(node.right, pp, qq) + (node.val == pp.val) + (node.val == qq.val)
                if now == 2:
                    if not self.ans:
                        self.ans = node
                return now
            else:
                return 0

        dfs(root, p, q)

        return self.ans


if __name__ == "__main__":
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.right))  # 3
    print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right.right))  # 5
