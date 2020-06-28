from toolkit import TreeNode, build_TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(node, maybe=False):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                if maybe:
                    return node.val
                else:
                    return 0
            elif node.right is None:
                return helper(node.left, maybe=True)
            elif node.left is None:
                return helper(node.right)
            else:
                return helper(node.left, maybe=True) + helper(node.right)

        return helper(root)


if __name__ == "__main__":
    print(Solution().sumOfLeftLeaves(build_TreeNode([3, 9, 20, None, None, 15, 7])))  # 24
