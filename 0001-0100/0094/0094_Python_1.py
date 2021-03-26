from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return []


if __name__ == "__main__":
    print(Solution().inorderTraversal(build_TreeNode([1, None, 2, 3])))  # [1,3,2]
