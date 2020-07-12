from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().preorderTraversal(build_TreeNode([1, None, 2, 3])))  # [1,2,3]
