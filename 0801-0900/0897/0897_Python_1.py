from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.root = None
        self.last = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node.left:
                helper(node.left)

            new_node = TreeNode(node.val)
            if self.root is None:
                self.root = self.last = new_node
            else:
                self.last.right = new_node
                self.last = self.last.right

            if node.right:
                helper(node.right)

        helper(root)

        return self.root


if __name__ == "__main__":
    tree = build_TreeNode([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
    print(Solution().increasingBST(tree))
    # [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
