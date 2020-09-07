from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        pass


if __name__ == "__main__":
    # [4,1,1,2,None,None,6,3,1,5]
    print(Solution().addOneRow(build_TreeNode([4, 2, 6, 3, 1, 5]), 1, 2))
