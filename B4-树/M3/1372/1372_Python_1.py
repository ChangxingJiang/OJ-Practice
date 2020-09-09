from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # 3
    print(Solution().longestZigZag(build_TreeNode([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1])))

    # 4
    print(Solution().longestZigZag(build_TreeNode([1, 1, 1, None, 1, None, None, 1, 1, None, 1])))

    # 0
    print(Solution().longestZigZag(build_TreeNode([1])))
