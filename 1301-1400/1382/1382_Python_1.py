from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def inorder(self, node, lst):
        if node:
            self.inorder(node.left, lst)
            lst.append(node.val)
            self.inorder(node.right, lst)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        self.inorder(root, lst)
        size = len(lst)
        return self.dfs(lst, 0, size - 1)

    def dfs(self, lst, l, r):
        if l > r:
            return None
        if l == r:
            return TreeNode(lst[l])
        else:
            m = (l + r) // 2
            root = TreeNode(lst[m])
            root.left = self.dfs(lst, l, m - 1)
            root.right = self.dfs(lst, m + 1, r)
            return root


if __name__ == "__main__":
    print(Solution().balanceBST(build_TreeNode([1, None, 2, None, 3, None, 4])))
