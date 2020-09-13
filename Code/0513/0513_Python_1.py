from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:

    def __init__(self):
        self.level = 0
        self.ans = None

    def findBottomLeftValue(self, root: TreeNode) -> int:
        def recursor(node, level=1):
            if node:
                # 判断是否为答案
                if level > self.level:
                    self.ans = node.val
                    self.level = level

                recursor(node.left, level + 1)
                recursor(node.right, level + 1)

        recursor(root)

        return self.ans


if __name__ == "__main__":
    # 1
    print(Solution().findBottomLeftValue(build_TreeNode([2, 1, 3])))

    # 7
    print(Solution().findBottomLeftValue(build_TreeNode([1, 2, 3, 4, None, 5, 6, None, None, 7])))
