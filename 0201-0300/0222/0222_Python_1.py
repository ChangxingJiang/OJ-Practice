from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1


if __name__ == "__main__":
    print(Solution().countNodes(build_TreeNode([1, 2, 3, 4, 5, 6])))  # 6
