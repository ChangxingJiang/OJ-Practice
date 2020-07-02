from toolkit import TreeNode, build_TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node):
            if not node:
                return []
            if node.left and node.right:
                return helper(node.left) + helper(node.right)
            elif node.left:
                return helper(node.left)
            elif node.right:
                return helper(node.right)
            else:
                return [node.val]

        return helper(root1) == helper(root2)


if __name__ == "__main__":
    tree1 = build_TreeNode([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
    tree2 = build_TreeNode([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    print(Solution().leafSimilar(tree1, tree2))  # True
