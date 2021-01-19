from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(now, node):
            if not node:
                return 0
            elif node.left and node.right:
                left = dfs(now + node.val, node.left)
                right = dfs(now + node.val, node.right)
                if now + node.val + left < limit:
                    node.left = None
                if now + node.val + right < limit:
                    node.right = None
                return node.val + max(left, right)
            elif node.left:
                left = dfs(now + node.val, node.left)
                return node.val + left
            elif node.right:
                right = dfs(now + node.val, node.right)
                return node.val + right
            else:
                return node.val

        val = dfs(0, root)
        return root if val >= limit else None


if __name__ == "__main__":
    # [1,2,3,4,null,null,7,8,9,null,14]
    print(Solution().sufficientSubset(build_TreeNode([1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]), 1))

    # [5,4,8,11,null,17,4,7,null,null,null,5]
    print(Solution().sufficientSubset(build_TreeNode([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]), 22))

    # []
    print(Solution().sufficientSubset(build_TreeNode([5, -6, -6]), 0))

    # [1,null,-3,4]
    print(Solution().sufficientSubset(build_TreeNode([1, 2, -3, -5, None, 4, None]), -1))
