from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [
    #    [5,4,11,2],
    #    [5,8,4,5]
    # ]
    tree = build_TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print(Solution().pathSum(tree, 22))
