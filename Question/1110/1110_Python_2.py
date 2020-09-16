from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def __init__(self):
        self.ans = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, delete):
            if node.left:
                if node.left.val in to_delete:
                    dfs(node.left, True)
                    node.left = None
                else:
                    if delete:
                        self.ans.append(node.left)
                    dfs(node.left, False)
            if node.right:
                if node.right.val in to_delete:
                    dfs(node.right, True)
                    node.right = None
                else:
                    if delete:
                        self.ans.append(node.right)
                    dfs(node.right, False)

        to_delete = set(to_delete)

        if not root:
            return []
        if not to_delete:
            return []

        if root.val in to_delete:
            self.ans = []
            dfs(root, True)
        else:
            self.ans = [root]
            dfs(root, False)

        return self.ans


if __name__ == "__main__":
    # [[1,2,null,4],[6],[7]]
    print(Solution().delNodes(build_TreeNode([1, 2, 3, 4, 5, 6, 7]), [3, 5]))
