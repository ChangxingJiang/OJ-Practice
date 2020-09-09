from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().flipEquiv(
        root1=build_TreeNode([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
        root2=build_TreeNode([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])))  # True
