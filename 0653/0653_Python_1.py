from toolkit import TreeNode, build_TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().findTarget(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 9))  # True
    print(Solution().findTarget(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 28))  # False
