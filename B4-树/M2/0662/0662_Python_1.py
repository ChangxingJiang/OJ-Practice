from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # 4
    print(Solution().widthOfBinaryTree(build_TreeNode([1, 3, 2, 5, 3, None, 9])))

    # 2
    print(Solution().widthOfBinaryTree(build_TreeNode([1, 3, None, 5, 3])))

    # 8
    print(Solution().widthOfBinaryTree(build_TreeNode([1, 3, 2, 5, None, None, 9, 6, None, None, 7])))
