from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isCompleteTree(build_TreeNode([1, 2, 3, 4, 5, 6])))  # True
    print(Solution().isCompleteTree(build_TreeNode([1, 2, 3, 4, 5, None, 7])))  # False
