from toolkit import TreeNode, build_TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    s1 = build_TreeNode([3, 4, 5, 1, 2])
    t1 = build_TreeNode([4, 1, 2])
    print(Solution().isSubtree(s1, t1))  # True
    s2 = build_TreeNode([3, 4, 5, 1, 2, None, None, 0, None])
    t2 = build_TreeNode([4, 1, 2])
    print(Solution().isSubtree(s2, t2))  # False
