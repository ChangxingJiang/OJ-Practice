from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.minimum = float("inf")
        self.last = float("-inf")

    def getMinimumDifference(self, root: TreeNode) -> int:
        def helper(node):
            if node:
                helper(node.left)

                self.minimum = min(self.minimum, node.val - self.last)
                self.last = node.val

                helper(node.right)

        helper(root)

        return int(self.minimum)


if __name__ == "__main__":
    print(Solution().getMinimumDifference(build_TreeNode([1, None, 3, 2, None])))  # 1
