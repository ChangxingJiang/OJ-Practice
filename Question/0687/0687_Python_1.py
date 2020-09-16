from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.max = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0

            left_length = 0
            right_length = 0
            if node.left:
                if node.val == node.left.val:
                    left_length = helper(node.left) + 1
                else:
                    helper(node.left)
            if node.right:
                if node.val == node.right.val:
                    right_length = helper(node.right) + 1
                else:
                    helper(node.right)
            if left_length > 0 and right_length > 0:
                self.max = max(self.max, left_length + right_length)
            else:
                self.max = max(self.max, left_length, right_length)
            return max(left_length, right_length)

        helper(root)

        return self.max


if __name__ == "__main__":
    print(Solution().longestUnivaluePath(build_TreeNode([5, 4, 5, 1, 1, None, 5])))  # 2
    print(Solution().longestUnivaluePath(build_TreeNode([1, 4, 5, 4, 4, None, 5])))  # 2
