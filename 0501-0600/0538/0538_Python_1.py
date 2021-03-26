from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)

        return root


if __name__ == "__main__":
    print(Solution().convertBST(build_TreeNode([5, 2, 13])))  # [18,20,13]
