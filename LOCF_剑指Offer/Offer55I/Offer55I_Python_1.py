from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    print(Solution().maxDepth(build_TreeNode([3, 9, 20, None, None, 15, 7])))  # 3
