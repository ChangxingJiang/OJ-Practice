from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else:
            return []


if __name__ == "__main__":
    print(Solution().preorderTraversal(build_TreeNode([1, None, 2, 3])))  # [1,2,3]
