from toolkit import TreeNode, build_TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


if __name__ == "__main__":
    print(Solution().insertIntoBST(build_TreeNode([4, 2, 7, 1, 3]), 5))  # [4,2,7,1,3,5]
    print(Solution().insertIntoBST(build_TreeNode([]), 5))  # [5]
