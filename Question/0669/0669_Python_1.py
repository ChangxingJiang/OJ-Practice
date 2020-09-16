from toolkit import TreeNode, build_TreeNode


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def helper(node):
            if not node:
                return None
            if L <= node.val <= R:
                node.left = helper(node.left)
                node.right = helper(node.right)
                return node
            elif node.val < L:
                return helper(node.right)
            elif node.val > R:
                return helper(node.left)

        return helper(root)


if __name__ == "__main__":
    print(Solution().trimBST(build_TreeNode([1, 0, 2]), 1, 2))  # [1,None,2]
    print(Solution().trimBST(build_TreeNode([3, 0, 4, None, 2, None, None, 1]), 1, 3))  # [3,2,None,1]
