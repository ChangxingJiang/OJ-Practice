from toolkit import TreeNode, build_TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(node):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    helper(node.left)
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    helper(node.right)

        if root is None:
            return TreeNode(val)
        else:
            helper(root)
            return root


if __name__ == "__main__":
    print(Solution().insertIntoBST(build_TreeNode([4, 2, 7, 1, 3]), 5))  # [4,2,7,1,3,5]
    print(Solution().insertIntoBST(build_TreeNode([]), 5))  # [5]
