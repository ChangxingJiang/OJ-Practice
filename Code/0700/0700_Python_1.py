from toolkit import TreeNode, build_TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(node):
            if not node:
                return None
            if val == node.val:
                return node
            elif val < node.val:
                return helper(node.left)
            else:
                return helper(node.right)

        return helper(root)


if __name__ == "__main__":
    print(Solution().searchBST(build_TreeNode([4, 2, 7, 1, 3]), 2))  # [2,1,3]
