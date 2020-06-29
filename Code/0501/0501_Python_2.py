from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def __init__(self):
        self.max_counter = 0
        self.now = None
        self.counter = 0

    def findMode(self, root: TreeNode) -> List[int]:

        res = []

        def helper(node):
            if not node:
                return None

            helper(node.left)

            if node.val == self.now:
                self.counter += 1
            else:
                self.counter = 0
                self.now = node.val

            if self.counter > self.max_counter:
                self.max_counter = self.counter
                res.clear()
                res.append(node.val)
            elif self.counter == self.max_counter:
                res.append(node.val)

            helper(node.right)

        helper(root)

        return res


if __name__ == "__main__":
    print(Solution().findMode(build_TreeNode([1, None, 2, 2])))  # 2
