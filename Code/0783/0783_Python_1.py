from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.min = float("inf")
        self.last = float("-inf")

    def minDiffInBST(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return []

            left = helper(node.left)

            self.min = min(self.min, node.val - self.last)
            self.last = node.val

            right = helper(node.right)

            return left + [node.val] + right

        helper(root)

        return int(self.min)


if __name__ == "__main__":
    print(Solution().minDiffInBST(build_TreeNode([4, 2, 6, 1, 3, None, None])))  # 1
    print(Solution().minDiffInBST(build_TreeNode([90, 69, None, 49, 89, None, 52, None, None, None, None])))  # 1
