from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().rightSideView(build_TreeNode([1, 2, 3, None, 5, None, 4])))  # [1,3,4]
