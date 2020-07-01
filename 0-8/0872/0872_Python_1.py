from toolkit import TreeNode, build_TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    tree1 = build_TreeNode([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
    tree2 = build_TreeNode([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    print(Solution().leafSimilar(tree1, tree2))  # True
