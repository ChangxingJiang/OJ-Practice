from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # 计算二叉树的最大深度
        def max_depth(node):
            if not node:
                return 0
            return max(max_depth(node.left), max_depth(node.right)) + 1

        def recursor(node):
            depth_left = max_depth(node.left)
            depth_right = max_depth(node.right)
            if depth_left == depth_right:
                return node
            else:
                return recursor(node.left) if depth_left > depth_right else recursor(node.right)

        return recursor(root)


if __name__ == "__main__":
    # [1,2,3]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3])))

    # [4]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3, 4])))

    # [2,4,5]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3, 4, 5])))
