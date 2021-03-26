from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = True

    def isValidBST(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode, min_val=float("-inf"), max_val=float("inf")):
        if root:
            if root.left and root.right:
                if not min_val < root.left.val < root.val < root.right.val < max_val:
                    self.ans = False
                else:
                    self.dfs(root.left, min_val=min_val, max_val=root.val)
                    self.dfs(root.right, min_val=root.val, max_val=max_val)
            elif root.left:
                if not min_val < root.left.val < root.val < max_val:
                    self.ans = False
                else:
                    self.dfs(root.left, min_val=min_val, max_val=root.val)
            elif root.right:
                if not min_val < root.val < root.right.val < max_val:
                    self.ans = False
                else:
                    self.dfs(root.right, min_val=root.val, max_val=max_val)


if __name__ == "__main__":
    # True
    print(Solution().isValidBST(build_TreeNode([2, 1, 3])))

    # False
    print(Solution().isValidBST(build_TreeNode([5, 1, 4, None, None, 3, 6])))
