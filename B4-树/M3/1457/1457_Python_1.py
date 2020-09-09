from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().pseudoPalindromicPaths(build_TreeNode([2, 3, 1, 3, 1, None, 1])))

    # 1
    print(Solution().pseudoPalindromicPaths(build_TreeNode([2, 1, 1, 1, 3, None, None, None, None, None, 1])))

    # 1
    print(Solution().pseudoPalindromicPaths(build_TreeNode([9])))
