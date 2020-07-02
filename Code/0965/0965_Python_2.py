from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.val = None

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.val = root.val

        def helper(node):
            if not node:
                return True
            elif node.val != self.val:
                return False
            else:
                return helper(node.left) and helper(node.right)

        return helper(root)


if __name__ == "__main__":
    tree = build_TreeNode([1, 1, 1, 1, 1, None, 1])
    print(Solution().isUnivalTree(tree))  # True
    tree = build_TreeNode([2, 2, 2, 5, 2])
    print(Solution().isUnivalTree(tree))  # False
