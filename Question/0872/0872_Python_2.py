from toolkit import TreeNode, build_TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from helper(node.left)
                yield from helper(node.right)

        return list(helper(root1)) == list(helper(root2))


if __name__ == "__main__":
    tree1 = build_TreeNode([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
    tree2 = build_TreeNode([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    print(Solution().leafSimilar(tree1, tree2))  # True

    tree1 = build_TreeNode([18, 35, 22, None, 103, 43, 101, 58, None, 97])
    tree2 = build_TreeNode([94, 102, 17, 122, None, None, 54, 58, 101, 97])
    print(Solution().leafSimilar(tree1, tree2))  # False
