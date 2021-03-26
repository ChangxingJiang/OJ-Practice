from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def inorder(self, node, lst):
        if node:
            self.inorder(node.left, lst)
            lst.append(node.val)
            self.inorder(node.right, lst)

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        lst1, lst2 = [], []
        self.inorder(root1, lst1)
        self.inorder(root2, lst2)

        s1, s2 = len(lst1), len(lst2)
        i1, i2 = 0, s2 - 1

        while i1 < s1 and i2 >= 0:
            val = lst1[i1] + lst2[i2]
            if val < target:
                i1 += 1
            elif val > target:
                i2 -= 1
            else:
                return True

        return False


if __name__ == "__main__":
    print(Solution().twoSumBSTs(build_TreeNode([2, 1, 4]), build_TreeNode([1, 0, 3]), 5))  # True
    print(Solution().twoSumBSTs(build_TreeNode([0, -10, 10]), build_TreeNode([5, 1, 7, 0, 2]), 18))  # False
    print(Solution().twoSumBSTs(build_TreeNode([0, -10, 10]), build_TreeNode([5, 1, 7, 0, 2]), 17))  # True
