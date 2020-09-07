from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        pass


if __name__ == "__main__":
    # [1,3,9]
    print(Solution().largestValues(build_TreeNode([1, 3, 2, 5, 3, None, 9])))
