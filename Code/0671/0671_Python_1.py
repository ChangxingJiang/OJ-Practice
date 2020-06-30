from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.min1 = float("inf")
        self.min2 = float("inf")

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def helper(node):
            if node.val < self.min1:
                self.min2 = self.min1
                self.min1 = node.val
            elif self.min1 < node.val < self.min2:
                self.min2 = node.val
            if node.left and node.right:
                if node.left.val < self.min2:
                    helper(node.left)
                if node.right.val < self.min2:
                    helper(node.right)

        helper(root)

        if self.min2 == float("inf"):
            return -1
        else:
            return int(self.min2)


if __name__ == "__main__":
    print(Solution().findSecondMinimumValue(build_TreeNode([2, 2, 5, None, None, 5, 7])))  # 5
    print(Solution().findSecondMinimumValue(build_TreeNode([2, 2, 2])))  # -1
    print(Solution().findSecondMinimumValue(build_TreeNode([2, 2, 5, None, None, 5, 5])))  # 5
