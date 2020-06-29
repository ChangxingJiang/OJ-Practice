from toolkit import TreeNode, build_TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    print(Solution().longestUnivaluePath(build_TreeNode([5, 4, 5, 1, 1, None, 5])))  # 2
    print(Solution().longestUnivaluePath(build_TreeNode([1, 4, 5, 4, 4, None, 5])))  # 2
