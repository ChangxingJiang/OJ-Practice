from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isSubStructure(build_TreeNode([1, 2, 3]), build_TreeNode([3, 1])))  # False
