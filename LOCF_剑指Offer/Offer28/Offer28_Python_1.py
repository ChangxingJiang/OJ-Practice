from toolkit import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
            elif node1 or node2:
                return False
            else:
                return True

        return dfs(root.left, root.right) if root else True


if __name__ == "__main__":
    print(Solution().isSymmetric(TreeNode([1, 2, 2, 3, 4, 4, 3])))  # True
    print(Solution().isSymmetric(TreeNode([1, 2, 2, None, 3, None, 3])))  # True
