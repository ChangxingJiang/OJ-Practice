from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        pass


if __name__ == "__main__":
    tree = build_TreeNode([1, 2, 5, 3, 4, None, 6])
    Solution().flatten(tree)
    print(tree)
