from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        pass


if __name__ == "__main__":
    # "dba"
    print(Solution().smallestFromLeaf(build_TreeNode([0, 1, 2, 3, 4, 3, 4])))

    # "adz"
    print(Solution().smallestFromLeaf(build_TreeNode([25, 1, 3, 1, 3, 0, 2])))

    # "abc"
    print(Solution().smallestFromLeaf(build_TreeNode([2, 2, 1, None, 1, 0, None, 0])))
