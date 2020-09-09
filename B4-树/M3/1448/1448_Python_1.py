from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # 4
    print(Solution().goodNodes(build_TreeNode([3, 1, 4, 3, None, 1, 5])))

    # 3
    print(Solution().goodNodes(build_TreeNode([3, 3, None, 4, 2])))

    # 1
    print(Solution().goodNodes(build_TreeNode([1])))
