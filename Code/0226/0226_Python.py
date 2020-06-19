from toolkit import TreeNode, build_TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if not node:
                return None
            node.left, node.right = helper(node.right), helper(node.left)
            return node

        return helper(root)


if __name__ == "__main__":
    print(Solution().invertTree(build_TreeNode([4, 2, 7, 1, 3, 6, 9])))  # [4,7,2,9,6,3,1]
