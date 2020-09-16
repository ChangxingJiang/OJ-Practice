from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.maximum = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            maximum = left + right
            if maximum > self.maximum:
                self.maximum = maximum
            return max(left, right) + 1

        depth(root)
        return self.maximum


if __name__ == "__main__":
    print(Solution().diameterOfBinaryTree(build_TreeNode([1, 2, 3, 4, 5])))  # 3
