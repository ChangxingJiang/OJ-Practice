from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        def recursor(node):
            # 处理当前节点不存在的情况
            if not node:
                return 0, 0

            # 左子树最大值(盗窃左节点和不盗窃左节点的两种情况)
            left1, left2 = recursor(node.left)

            # 右子树最大值(盗窃右节点和不盗窃右节点的两种情况)
            right1, right2 = recursor(node.right)

            # 盗窃当前节点并继续向根节点盗窃所能提供的最大值
            most_maybe1 = node.val + left2 + right2

            # 不盗窃当前节点并继续向根节点盗窃所能提供的最大值
            most_maybe2 = max(left1, left2) + max(right1, right2)  # 使用左子树和右子树的最大值，不盗窃当前节点

            return most_maybe1, most_maybe2

        return max(recursor(root))


if __name__ == "__main__":
    print(Solution().rob(build_TreeNode([3, 2, 3, None, 3, None, 1])))  # 7
    print(Solution().rob(build_TreeNode([3, 4, 5, 1, 3, None, 1])))  # 9
    print(Solution().rob(build_TreeNode([4, 2, None, 1, 3])))  # 9
