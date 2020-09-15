from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
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
    # [2,7,4]
    print(Solution().subtreeWithAllDeepest(build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])))
