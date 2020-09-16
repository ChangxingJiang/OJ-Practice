from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.max = 0

    def maxProduct(self, root: TreeNode) -> int:
        # 处理特殊情况
        if not root:
            return self.max

        # 计算子树和
        def dfs_sum(node):
            if node:
                if node.left:
                    dfs_sum(node.left)
                    node.val += node.left.val
                if node.right:
                    dfs_sum(node.right)
                    node.val += node.right.val

        dfs_sum(root)

        total = root.val

        # 计算最大乘积
        def dfs_count(node):
            if node:
                if node.left:
                    a = node.left.val
                    b = total - node.left.val
                    self.max = max(self.max, a * b)
                    if a > b:
                        dfs_count(node.left)
                if node.right:
                    a = node.right.val
                    b = total - node.right.val
                    self.max = max(self.max, a * b)
                    if a > b:
                        dfs_count(node.right)

        dfs_count(root)

        return self.max % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().maxProduct(build_TreeNode([1, 2, 3, 4, 5, 6])))  # 110
    print(Solution().maxProduct(build_TreeNode([1, None, 2, 3, 4, None, None, 5, 6])))  # 90
    print(Solution().maxProduct(build_TreeNode([2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1])))  # 1025
    print(Solution().maxProduct(build_TreeNode([1, 1])))  # 1
