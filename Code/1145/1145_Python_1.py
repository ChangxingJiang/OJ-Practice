from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.choose_3 = -1  # 二号玩家选项3：一号玩家的右子节点
        self.choose_2 = -1  # 二号玩家选项2：一号玩家的左子节点
        self.choose_1 = -1  # 二号玩家选项1：一号玩家的父节点

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def dfs(node):
            if not node:
                return 0
            if node.val == x:
                self.choose_2 = dfs(node.left)
                self.choose_3 = dfs(node.right)
                self.choose_1 = n - self.choose_2 - self.choose_3 - 1
                return self.choose_2 + self.choose_3 + 1
            else:
                return dfs(node.left) + dfs(node.right) + 1

        dfs(root)

        point2 = max(self.choose_1, self.choose_2, self.choose_3)
        point1 = sum([self.choose_1, self.choose_2, self.choose_3]) - point2

        return point2 > point1


if __name__ == "__main__":
    # True
    print(Solution().btreeGameWinningMove(build_TreeNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 11, 3))

    # False
    print(Solution().btreeGameWinningMove(build_TreeNode([1, 2, 3]), 3, 1))
