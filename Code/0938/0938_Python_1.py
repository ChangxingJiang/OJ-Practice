from toolkit import TreeNode, build_TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def helper(node):
            if not node:
                return 0
            ans = 0
            if L <= node.val <= R:
                ans += node.val
            if L < node.val:
                ans += helper(node.left)
            if R > node.val:
                ans += helper(node.right)
            return ans

        return helper(root)


if __name__ == "__main__":
    print(Solution().rangeSumBST(build_TreeNode([10, 5, 15, 3, 7, None, 18]), 7, 15))  # 32
    print(Solution().rangeSumBST(build_TreeNode([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10))  # 23
