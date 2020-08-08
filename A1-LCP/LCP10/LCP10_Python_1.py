from toolkit import TreeNode, build_TreeNode


class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        pass


if __name__ == "__main__":
    print(Solution().minimalExecTime(build_TreeNode([47, 74, 31])))  # 121
    print(Solution().minimalExecTime(build_TreeNode([15, 21, None, 24, None, 27, 26])))  # 87
    print(Solution().minimalExecTime(build_TreeNode([1, 3, 2, None, None, 4, 4])))  # 7.5
