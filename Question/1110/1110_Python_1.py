from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.ans.append(root)
        to_delete = set(to_delete)

        def dfs(node):
            if node:
                left = node.left
                right = node.right
                if node.val in to_delete:
                    if node in self.ans:
                        self.ans.remove(node)
                        to_delete.remove(node.val)
                    if node.left:
                        self.ans.append(node.left)
                    if node.right:
                        self.ans.append(node.right)
                else:
                    if node.left and node.left.val in to_delete:
                        node.left = None
                    if node.right and node.right.val in to_delete:
                        node.right = None
                if to_delete:
                    dfs(left)
                    dfs(right)

        dfs(root)
        return self.ans


if __name__ == "__main__":
    # [[1,2,null,4],[6],[7]]
    print(Solution().delNodes(build_TreeNode([1, 2, 3, 4, 5, 6, 7]), [3, 5]))
