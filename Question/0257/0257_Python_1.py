from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def helper(node, path=None):
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)
            if node.left and node.right:
                return helper(node.left, path) + helper(node.right, path)
            elif node.left:
                return helper(node.left, path)
            elif node.right:
                return helper(node.right, path)
            else:
                return [path]

        if root:
            return helper(root)
        else:
            return []


if __name__ == "__main__":
    tree = build_TreeNode([1, 2, 3, None, 5])
    print(Solution().binaryTreePaths(tree))  # [[1,3],[1,2,5]]
