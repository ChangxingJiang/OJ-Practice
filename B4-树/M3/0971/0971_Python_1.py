from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2]), [2, 1]))  # [-1]
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2, 3]), [1, 3, 2]))  # [1]
    print(Solution().flipMatchVoyage(build_TreeNode([1, 2, 3]), [1, 2, 3]))  # []
