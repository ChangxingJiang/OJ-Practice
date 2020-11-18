from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.aim = None
        self.ans = None
        self.this = False  # 上一个为目标节点

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.aim = p
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            self.dfs(node.left)

            if self.this:
                self.ans = node
                self.this = False
            else:
                if node == self.aim:
                    self.this = True

                if node.right:
                    self.dfs(node.right)


if __name__ == "__main__":
    # 2
    tree = build_TreeNode([2, 1, 3])
    print(Solution().inorderSuccessor(tree, tree.left))

    # None
    tree = build_TreeNode([5, 3, 6, 2, 4, None, None, 1])
    print(Solution().inorderSuccessor(tree, tree.right))
