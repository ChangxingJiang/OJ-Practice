from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        pass


if __name__ == "__main__":
    # [3,1,None,None,2]
    print(Solution().recoverTree(build_TreeNode([1, 3, None, None, 2])))

    # [2,1,4,None,None,3]
    print(Solution().recoverTree(build_TreeNode([2, 1, 4, None, None, 3])))
