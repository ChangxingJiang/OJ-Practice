from toolkit import TreeNode, build_TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        pass


if __name__ == "__main__":
    tree = build_TreeNode([[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]])
    print(Solution().pathSum(tree, 8))  # 3
