from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        MOD = 10 ** 9 + 7
        self.max = -MOD

    def maxPathSum(self, root: TreeNode) -> int:
        self.count_max(root)
        return self.max

    def count_max(self, root: TreeNode) -> int:
        # 处理有两个子树的情况
        if root.left and root.right:
            left_max = self.count_max(root.left)
            right_max = self.count_max(root.right)
            if left_max >= 0 and right_max >= 0:
                self.max = max(self.max, root.val + left_max + right_max)
                return root.val + max(left_max, right_max)
            elif left_max >= 0:
                res_max = root.val + left_max
                self.max = max(self.max, res_max)
                return res_max
            elif right_max >= 0:
                res_max = root.val + right_max
                self.max = max(self.max, res_max)
                return res_max
            else:
                self.max = max(self.max, root.val)
                return root.val

        # 处理只有左子树的情况
        elif root.left:
            left_max = self.count_max(root.left)
            if left_max >= 0:
                res_max = root.val + left_max
                self.max = max(self.max, res_max)
                return res_max
            else:
                self.max = max(self.max, root.val)
                return root.val

        # 处理只有右子树的情况
        elif root.right:
            right_max = self.count_max(root.right)
            if right_max >= 0:
                res_max = root.val + right_max
                self.max = max(self.max, res_max)
                return res_max
            else:
                self.max = max(self.max, root.val)
                return root.val

        # 处理叶节点的情况
        else:
            self.max = max(self.max, root.val)
            return root.val


if __name__ == "__main__":
    print(Solution().maxPathSum(build_TreeNode([1, 2, 3])))  # 6
    print(Solution().maxPathSum(build_TreeNode([-10, 9, 20, None, None, 15, 7])))  # 42
