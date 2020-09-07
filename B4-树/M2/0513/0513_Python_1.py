from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # 1
    print(Solution().findBottomLeftValue(build_TreeNode([2, 1, 3])))

    # 7
    print(Solution().findBottomLeftValue(build_TreeNode([1, 2, 3, 4, None, 5, 6, None, None, 7])))
