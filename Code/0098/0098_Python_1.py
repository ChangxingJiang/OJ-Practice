from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def isValidBST(self, root: TreeNode, left=float("-inf"), right=float("inf")) -> bool:
        if not root:
            return True
        if root.left:
            if not left < root.left.val < root.val:
                return False
            if not self.isValidBST(root.left, left=left, right=root.val):
                return False
        if root.right:
            if not root.val < root.right.val < right:
                return False
            if not self.isValidBST(root.right, left=root.val, right=right):
                return False
        return True


if __name__ == "__main__":
    print(Solution().isValidBST(build_TreeNode([2, 1, 3])))  # True
    print(Solution().isValidBST(build_TreeNode([5, 1, 4, None, None, 3, 6])))  # False
    print(Solution().isValidBST(build_TreeNode([10, 5, 15, None, None, 6, 20])))  # False
    print(Solution().isValidBST(build_TreeNode([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])))  # False
