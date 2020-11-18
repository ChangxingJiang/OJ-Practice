from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0
        self.sum = 0
        self.total = 0
        self.lst = []

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        self.sum = sum

        self.dfs(root)

        return self.ans

    def dfs(self, node):
        self.total += node.val
        self.lst.append(node.val)

        last = 0
        for i in range(len(self.lst) - 1, -1, -1):
            last += self.lst[i]
            if last == self.sum:
                self.ans += 1

        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)

        # print(self.total, self.lst, self.ans)

        self.lst.pop()
        self.total -= node.val


if __name__ == "__main__":
    # 3
    print(Solution().pathSum(build_TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))

    # 1
    print(Solution().pathSum(build_TreeNode([-2, None, -3]), -3))

    # 4
    print(Solution().pathSum(build_TreeNode([0, 1, 1]), 1))
