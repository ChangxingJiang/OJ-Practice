from toolkit import TreeNode, build_TreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isCousins(build_TreeNode([1, 2, 3, 4]), 4, 3))  # False
    print(Solution().isCousins(build_TreeNode([1, 2, 3, None, 4, None, 5]), 5, 4))  # True
    print(Solution().isCousins(build_TreeNode([1, 2, 3, None, 4]), 2, 3))  # False
