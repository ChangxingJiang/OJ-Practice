from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def sumNumbers(self, root: TreeNode) -> int:
        self.count(root)
        return self.ans

    def count(self, node, now_val=0):
        if node:
            new_val = now_val * 10 + node.val
            if not node.left and not node.right:
                self.ans += new_val
            self.count(node.left, new_val)
            self.count(node.right, new_val)


if __name__ == "__main__":
    print(Solution().sumNumbers(build_TreeNode([1, 2, 3])))  # 25
    print(Solution().sumNumbers(build_TreeNode([4, 9, 0, 5, 1])))  # 1026
