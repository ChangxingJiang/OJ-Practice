from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        pass


if __name__ == "__main__":
    tree = build_TreeNode([1, 2, 3, None, 5])
    print(Solution().binaryTreePaths(tree))  # [[1,3],[1,2,5]]
