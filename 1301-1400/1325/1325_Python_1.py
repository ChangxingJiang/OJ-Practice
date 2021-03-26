from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node):
            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None
            return not node.left and not node.right and node.val == target

        dfs(root)

        if not root.left and not root.right and root.val == target:
            return None

        return root


if __name__ == "__main__":
    # [1,null,3,null,4]
    print(Solution().removeLeafNodes(build_TreeNode([1, 2, 3, 2, None, 2, 4]), 2))

    # [1,3,null,null,2]
    print(Solution().removeLeafNodes(build_TreeNode([1, 3, 3, 3, 2]), 3))

    # [1]
    print(Solution().removeLeafNodes(build_TreeNode([1, 2, None, 2, None, 2]), 2))

    # []]
    print(Solution().removeLeafNodes(build_TreeNode([1, 1, 1]), 1))

    # [1,2,3]
    print(Solution().removeLeafNodes(build_TreeNode([1, 2, 3]), 1))
