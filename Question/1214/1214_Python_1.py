from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False

        if root1.val + root2.val < target:
            return self.twoSumBSTs(root1.right, root2, target) or self.twoSumBSTs(root1, root2.right, target)
        elif root1.val + root2.val > target:
            return self.twoSumBSTs(root1.left, root2, target) or self.twoSumBSTs(root1, root2.left, target)
        else:
            return True


if __name__ == "__main__":
    print(Solution().twoSumBSTs(build_TreeNode([2, 1, 4]), build_TreeNode([1, 0, 3]), 5))  # True
    print(Solution().twoSumBSTs(build_TreeNode([0, -10, 10]), build_TreeNode([5, 1, 7, 0, 2]), 8))  # False
