from toolkit import TreeNode, build_TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    print(Solution().findSecondMinimumValue(build_TreeNode([2, 2, 5, None, None, 5, 7])))  # 5
    print(Solution().findSecondMinimumValue(build_TreeNode([2, 2, 2])))  # -1
