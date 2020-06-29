from toolkit import TreeNode, build_TreeNode


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        pass


if __name__ == "__main__":
    print(Solution().trimBST(build_TreeNode([1, 0, 2]), 1, 2))  # [1,None,2]
    print(Solution().trimBST(build_TreeNode([0, 3, 4, None, 2, None, None, 1]), 1, 3))  # [3,2,None,1]
