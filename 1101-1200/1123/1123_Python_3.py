from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node, depth):
            if not node:
                return None, 0
            if not node.left and not node.right:
                return node, depth
            left, depth_left = dfs(node.left, depth + 1)
            right, depth_right = dfs(node.right, depth + 1)
            if depth_left == depth_right:
                return node, depth_left
            elif depth_left > depth_right:
                return left, depth_left
            else:
                return right, depth_right

        return dfs(root, 1)[0]


if __name__ == "__main__":
    # [1,2,3]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3])))

    # [4]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3, 4])))

    # [2,4,5]
    print(Solution().lcaDeepestLeaves(build_TreeNode([1, 2, 3, 4, 5])))
