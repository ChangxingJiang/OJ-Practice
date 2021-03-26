from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = None

    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        self.dfs(root, u)
        return self.ans

    # 寻找目标节点
    def dfs(self, node, u):
        if not node:
            return -1
        if node == u:
            return 0
        else:
            left = self.dfs(node.left, u)
            if left != -1 and self.ans is None:
                self.dfs2(node.right, left + 1)
                return left + 1

            right = self.dfs(node.right, u)
            if right != -1:
                return right + 1

            return -1

    # 寻找目标节点的右侧节点（即寻找当前节点的等层最左侧节点）
    # O(logN)
    def dfs2(self, node, num):
        if node:
            if num == 1:
                self.ans = node
            else:
                if self.ans is None and node.left:
                    self.dfs2(node.left, num - 1)
                if self.ans is None and node.right:
                    self.dfs2(node.right, num - 1)


if __name__ == "__main__":
    # 5
    tree = build_TreeNode([1, 2, 3, None, 4, 5, 6])
    print(Solution().findNearestRightNode(tree, tree.left.right))

    # None
    tree = build_TreeNode([3, None, 4, 2])
    print(Solution().findNearestRightNode(tree, tree.right.left))

    # None
    tree = build_TreeNode([1])
    print(Solution().findNearestRightNode(tree, tree))

    # 2
    tree = build_TreeNode([3, 4, 2, None, None, None, 1])
    print(Solution().findNearestRightNode(tree, tree.left))
