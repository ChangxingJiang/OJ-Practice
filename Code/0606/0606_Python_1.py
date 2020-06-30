from toolkit import TreeNode, build_TreeNode


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def helper(node):
            if not node:
                return ""
            if node.left and node.right:
                return str(node.val) + "(" + helper(node.left) + ")(" + helper(node.right) + ")"
            elif node.left:
                return str(node.val) + "(" + helper(node.left) + ")"
            elif node.right:
                return str(node.val) + "()(" + helper(node.right) + ")"
            else:
                return str(node.val)

        return helper(t)


if __name__ == "__main__":
    print(Solution().tree2str(build_TreeNode([1, 2, 3, 4])))  # 1(2(4))(3)
    print(Solution().tree2str(build_TreeNode([1, 2, 3, None, 4])))  # 1(2()(4))(3)
