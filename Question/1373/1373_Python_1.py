from LeetTool import TreeNode
from LeetTool import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def maxSumBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return True, 0, float("inf"), float("-inf")
        else:
            # 遍历两棵子树
            bool1, val1, l1, l2 = self.dfs(node.left)
            bool2, val2, r1, r2 = self.dfs(node.right)

            # 判断两棵子树是否符合二叉搜索树性质
            if not bool1 or not bool2:
                return False, -1, 0, 0

            # 判断当前节点是否符合二叉搜索树性质
            if node.val <= l2 or node.val >= r1:
                return False, -1, 0, 0

            l = l1 if node.left else node.val
            r = r2 if node.right else node.val

            val = val1 + node.val + val2
            self.ans = max(self.ans, val)
            return True, val, l, r


if __name__ == "__main__":
    print(Solution().maxSumBST(build_TreeNode([1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6])))  # 20
    print(Solution().maxSumBST(build_TreeNode([4, 3, None, 1, 2])))  # 2
    print(Solution().maxSumBST(build_TreeNode([-4, -2, -5])))  # 0
    print(Solution().maxSumBST(build_TreeNode([2, 1, 3])))  # 6
    print(Solution().maxSumBST(build_TreeNode([5, 4, 8, 3, None, 6, 3])))  # 7
    print(Solution().maxSumBST(build_TreeNode([1, None, 10, -5, 20])))  # 25
    print(Solution().maxSumBST(build_TreeNode([8, 9, 8, None, 9, None, 1, None, None, -3, 5, None, -2, None, 6])))  # 11
