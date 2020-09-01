from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isValidBST(build_TreeNode([2, 1, 3])))  # True
    print(Solution().isValidBST(build_TreeNode([5, 1, 4, None, None, 3, 6])))  # False
