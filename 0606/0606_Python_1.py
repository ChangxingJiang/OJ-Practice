from toolkit import TreeNode, build_TreeNode


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        pass


if __name__ == "__main__":
    print(Solution().tree2str(build_TreeNode([1, 2, 3, 4])))  # 1(2(4))(3)
    print(Solution().tree2str(build_TreeNode([1, 2, 3, None, 4])))  # 1(2()(4))(3)
