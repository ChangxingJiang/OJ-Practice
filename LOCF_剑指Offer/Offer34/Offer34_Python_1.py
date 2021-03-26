from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.lst = []
        self.val = 0
        self.ans = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node):
            if node:
                self.val += node.val
                self.lst.append(node.val)
                if node.left or node.right:
                    if node.left:
                        dfs(node.left)
                    if node.right:
                        dfs(node.right)
                else:
                    if self.val == sum:
                        self.ans.append(self.lst.copy())
                self.val -= node.val
                self.lst.pop()

        dfs(root)

        return self.ans


if __name__ == "__main__":
    # [
    #    [5,4,11,2],
    #    [5,8,4,5]
    # ]
    tree = build_TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print(Solution().pathSum(tree, 22))
