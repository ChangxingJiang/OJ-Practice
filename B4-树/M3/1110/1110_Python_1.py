from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        pass


if __name__ == "__main__":
    # [[1,2,null,4],[6],[7]]
    print(Solution().delNodes(build_TreeNode([1, 2, 3, 4, 5, 6, 7]), [3, 5]))
