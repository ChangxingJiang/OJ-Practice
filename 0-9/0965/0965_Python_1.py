from toolkit import TreeNode, build_TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    tree = build_TreeNode([1, 1, 1, 1, 1, None, 1])
    print(Solution().isUnivalTree(tree))  # True
    tree = build_TreeNode([2, 2, 2, 5, 2])
    print(Solution().isUnivalTree(tree))  # False
