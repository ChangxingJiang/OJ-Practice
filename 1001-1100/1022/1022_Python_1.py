from toolkit import TreeNode, build_TreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def helper(node, value=""):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return int(value + str(node.val), base=2)
            else:
                return helper(node.left, value + str(node.val)) + helper(node.right, value + str(node.val))

        return helper(root)


if __name__ == "__main__":
    print(Solution().sumRootToLeaf(build_TreeNode([1, 0, 1, 0, 1, 0, 1])))  # 22
