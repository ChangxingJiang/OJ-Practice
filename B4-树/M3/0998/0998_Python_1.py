from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        pass


if __name__ == "__main__":
    # [5,4,null,1,3,null,null,2]
    print(Solution().insertIntoMaxTree(build_TreeNode([4, 1, 3, None, None, 2]), 5))

    # [5,2,4,null,1,null,3]
    print(Solution().insertIntoMaxTree(build_TreeNode([5, 2, 4, None, 1]), 3))

    # [5,2,4,null,1,3]
    print(Solution().insertIntoMaxTree(build_TreeNode([5, 2, 3, None, 1]), 4))
